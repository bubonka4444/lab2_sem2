import numpy as np
from numpy import linalg

matrix = int(input('Введите размерность квадратной матрицы больше 1 и меньше 20:'))
while (matrix < 1) or (matrix > 20):
    matrix = int(input("Введите указанные числа"))
size = np.random.randint(5, size=(matrix, matrix))
print("Матрица:\n", size)

sign = int(input('Кол-во знаков после запятой:'))
sign = 0.1 ** sign
n = 1
factorial = 1
summ = 0
fg = 0
out = 1
while abs(out) > sign:
    fg += summ
    summ += np.linalg.det(linalg.matrix_power(size, 2 * n)) / factorial
    n += 1
    factorial *= (2*n -1) * (2*n)
    out = abs(fg-summ)
    fg = 0
    print(n-1, ':', summ, ' ', out)
print('Сумма знакопеременного ряда:', summ)