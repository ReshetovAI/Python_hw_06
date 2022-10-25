# Задача 2. Найти сумму чисел списка стоящих на нечетной позиции


from random import randint


# def get_list(n, frst, last):
#     return [randint(frst, last) for i in range(n)]


# def sum_odd_position(my_list):
#     return sum(my_list[1::2])


# n = 5
# frst = 1
# last = 10

# my_list = get_list(n, frst, last)
# print('Заданный список: ', my_list)
# print('Элементы стоящие на нечетных позициях: ', my_list[1::2])
# print('Сумма элементов стоящих на нечетной позиции = ', sum_odd_position(my_list))


#
import random


def list_generation():
    n = int(input('Количество элементов списка: '))
    b1 = int(input('Граница 1 диапазона значений элементов списка: '))
    b2 = int(input('Граница 2 диапазона значений элементов списка: '))
    return [random.randint(min(b1, b2), max(b1, b2)) for i in range(n)]


numbers_list = list_generation()

sum_odd = sum(numbers_list[item] for item in range(1, len(numbers_list), 2))
odd_el = str([numbers_list[item]
             for item in range(1, len(numbers_list), 2)]).strip('[]')
print(
    f'Для списка {numbers_list} сумма чисел, стоящих на нечётных позициях: \n{odd_el} равна {sum_odd}.')
