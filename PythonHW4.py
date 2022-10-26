# Вычислить число c заданной точностью d

#numm = float(input('Введите число: '))
#d = float(input('Введите точность округления числа: '))

#if d == 1:
#    print(int(n))
#else: 
#    d = str(d)
#    d = d.split('.')
#    d = len(d[1])
#print(round(numm, d))


# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

#n = int(input('Введите число: '))
#some_list = []

#for i in range(2, n + 1):
#    if n % i == 0:
#        for j in range (2, i//2 + 1):
#            if i % j == 0:
#                break
#        else:
#            some_list.append(i)
#print(some_list)


# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности

#count = int(input('Введите количество элементов: '))
#some_list = []
#for _ in range (count):
#    number = int(input())
#    some_list.append(number)
#print(f'Ваш список элементов: {some_list}')
#new_list = []
#for i in some_list:
#    count = 0
#    for j in some_list:
#        if i == j:
#            count += 1
#        if count == 2:
#            break
#    if count == 1:
#        new_list.append(i)
#print(f'Неповторяющиеся элементы введенного списка: {new_list}')


#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

from random import randint


k = int(input('Введите натуральную степень k: '))

koeff=[randint(0, 100) for i in range(k)]+[randint(1, 100)]
poly='+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(koeff) if j][::-1])

poly=poly.replace('x^1+', 'x+')
poly=poly.replace('x^0', '')
poly+=('','1')[poly[-1]=='+']
poly=(poly, poly[:-2])[poly[-2:]=='^1']
print(f'{poly} = 0')

with open ('text.txt', 'w', encoding='utf-8') as f:
    f.write(f'{poly} = 0')


