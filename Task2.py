# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
#  Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4
def summa(a, b):
    if a == 1 and b == 1:
        return 2
    if a != 1 and b == 1:
        return summa(1, a-1) + b
    if a == 1 and b !=1:
        return a + summa(1, b-1)
    return summa(1,a-1) + summa(1, b-1)
print(summa(int(input('First num: ')), int(input('Second num: '))))
    