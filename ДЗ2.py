'''Для натурального n создать словарь индекс-значение, состоящий из элементов
последовательности 3n + 1.
Пример: Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}'''
# n = int(input('Введите число: '))
# d = {a: a * 3 + 1 for a in range(1, n+1)}
# print(d)
# 'ИЛИ'
# n = int(input('Введите число: '))
# d = {}
# for i in range(1, n+1):
#     key = i
#     val = 3*i + 1
#     d[key] = val
# print(d)

'''Напишите программу, которая принимает на вход число N
и выдает набор произведений чисел от 1 до N.
Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)'''
# n = int(input('Введите число: '))
# f = 1
# for i in range(1, n+1):
#     f *= i
#     print(f, end=', ')

'''Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.
Пример: Для n = 5: сумма = 11,55'''
# n = int(input('Введите число: '))
# lst = []
# x = 1
# for i in range(n):
#     lst.append((1+(1/x))**x)
#     x += 1
# sum = 0
# for i in lst:
#     sum = sum + i
# print('сумма =', round(sum, 2))

'''Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях.
Позиции хранятся в файле file.txt в одной строке одно число.'''
# n = int(input('Введите число: '))
# lst = []
# for i in range(-n, n+1):
#     lst.append(i)
# print(lst)
# f = open('file.txt')
# ind1 = int(f.read(1))
# ind2 = int(f.read(2))
# f.close()
# print(ind1, 'and', ind2)
# mult = lst[ind1] * lst[ind2]
# print(lst[ind1], '*', lst[ind2], '=', mult)



'''Реализуйте алгоритм перемешивания списка.(Без использования библиотеки random)'''
# n = int(input('Размер массива: '))
# lst = []
# for i in range(n):
#     x = int(input('Введите число массива: '))
#     lst.append(x)
# print(lst)
# import datetime
# for i in range(0, len(lst)):
#     j = datetime.datetime.now().microsecond % len(lst) - 1
#     lst[i], lst[j] = lst[j], lst[i]
#     print(datetime.datetime.now().microsecond)
# print(lst)