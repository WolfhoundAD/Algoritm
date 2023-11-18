#Задача №1
#Это приложение моделирует задачу планирования расписания. Оно использует структуры данных (списки) и алгоритм сортировки для
# определения минимального количества перегрузок времени между задачами. Путем сортировки времен начала и окончания задач и 
#последующего анализа, программа определяет, перегрузок временb потребуется для выполнения всех задач.
class Task:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def min_meeting_rooms(tasks):
    if not tasks:
        return 0

    # Создаем список начал и окончаний задач
    start_times = [task.start for task in tasks]
    end_times = [task.end for task in tasks]

    # Сортируем времена начала и окончания
    start_times.sort()
    end_times.sort()

    rooms_needed = 0
    end_pointer = 0

    for start_time in start_times:
        if start_time < end_times[end_pointer]:
            rooms_needed += 1
        else:
            end_pointer += 1

    return rooms_needed


tasks_list = [Task(9, 10), Task(9, 12), Task(10, 11), Task(11, 13), Task(14, 15)]

result = min_meeting_rooms(tasks_list)
print(f"Результат задачи №1:Минимальное необходимое время: {result}")


#Задача №2
#Этот пример использует структуру данных словаря (frequency), чтобы подсчитать количество встреч каждого элемента в списке. 
# Путем прохода по списку и увеличения счетчика для каждого элемента, программа определяет элемент с наибольшей частотой 
# встречаемости и выводит его. Это пример использования алгоритма подсчета частоты встречаемости элементов в списке.
def most_frequent_element(arr):
    if not arr:
        return None

    frequency = {}
    max_frequency = 0
    most_frequent = None

    for item in arr:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1

        if frequency[item] > max_frequency:
            max_frequency = frequency[item]
            most_frequent = item

    return most_frequent


numbers = [1, 3, 5, 2, 1, 5, 2, 2, 5, 5, 5]
result = most_frequent_element(numbers)

if result is not None:
    print(f"Результат задачи №2:Наиболее часто встречающийся элемент в списке {numbers}: {result}")
else:
    print("Список пуст.")


#Задача №3
#Палиндром - это строка, которая читается одинаково как слева направо, так и справа налево.
#Этот пример использует структуру данных строки и алгоритм двух указателей для проверки строки на палиндромность.
#  Он приводит строку к нижнему регистру, удаляет пробелы и затем сравнивает символы с обоих концов строки,
#  игнорируя знаки препинания и различия в регистре. Если строки читаются одинаково с обоих сторон, то это палиндром,
#  и программа выводит соответствующий результат.
def is_palindrome(string):
    # Приводим строку к нижнему регистру и удаляем пробелы
    processed_string = string.lower().replace(" ", "")
    
    # Используем два указателя для сравнения символов с обоих концов строки
    left, right = 0, len(processed_string) - 1
    
    while left < right:
        if processed_string[left] != processed_string[right]:
            return False
        left += 1
        right -= 1
        
    return True


test_string = "dAB ssB A d"
result = is_palindrome(test_string)

if result:
    print(f"Строка '{test_string}' является палиндромом.")
else:
    print(f"Строка '{test_string}' не является палиндромом.")
