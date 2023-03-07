""""
Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума)

Ввод: [-5, 9, 0, 3, -1, -2, 1,
4, -2, 10, 2, 0, -9, 8, 10, -9,
0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]
"""

# Создаем функцию для заполнения массива


def inputArray(size):
    array = []
    for i in range(size):
        array.append(int(input()))
    return array


# Создаем массив с помощью вызова функции
sizeArray = int(input("Введите размер первого массива: "))
array_1 = inputArray(sizeArray)
print(array_1)

# Определяем минимальное значение и максимальное значение элемента

num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))

if num_1 > num_2:
    maxNum = num_1
    minNum = num_2
else:
    maxNum = num_2
    minNum = num_1

for i in range(len(array_1)):
    if array_1[i] < maxNum and array_1[i] > minNum:
        print(i)
