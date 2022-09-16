# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# from math import pi
# d =  int(input("Введите значение для заданной точности числа ПИ: "))
# print(f"Число ПИ = {round(pi, d)}")

# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

# def cheking(n: int):
#     i = 2
#     while n % i != 0 or i == n - 1:
#         i += 1
#     if i == n:
#         return n
# def my_list (n: int) -> list:
#     simpleNumber_list = [1]
#     for i in range(2, n + 1):
#         if n % i == 0:
#             if cheking(i) != None:
#                 simpleNumber_list.append(cheking(i))
#             else:
#                 continue
#     return simpleNumber_list
# N = int(input('Введите число N: '))
# simple_list = my_list(N)
# print(simple_list)

# Задайте последовательность чисел. Напишите программу,
#  которая выведет список неповторяющихся элементов исходной последовательности.

# my_list = input("Введите числа: ").split()
# numbers = []
# temp = []
# for i in range(len(my_list)):
#     if (my_list[i] in my_list[i + 1:]) or (my_list[i] in temp):
#         temp.append(my_list[i])
#     else:
#         numbers.append(int(my_list[i]))
# print(numbers)

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
#  (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
k = int(input('Введите коэффициент: '))
FirstN = int(random.randint(0,100))
SecondN = int(random.randint(0,100))
ThirdN = int(random.randint(0,100))
if FirstN != 0:
    first = (str(FirstN) + "x^" + str(k) + " + ")
else:
    first = (str())
if SecondN != 0:
    second = (str(SecondN) + "x" + " + ")
else:
    second = (str())
if ThirdN != 0:
    third = (str(ThirdN) + " = 0")
else:
    third = (str())
print(f'{first}{second}{third}')