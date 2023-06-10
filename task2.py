#Напишите функцию print_operation_table(operation, num_rows=6, 
#num_columns=6), которая принимает в качестве аргумента функцию, 
#вычисляющую элемент по номеру строки и столбца, т.е.
# функцию двух аргументов. Аргументы num_rows и num_columns указывают 
#число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы.
#Примеры/Тесты:
#print_operation_table(lambda x,y: x**y,4,4)
#1   1   1   1
#2   4   8  16
#3   9  27  81
#4  16  64 256
def print_operation_table(operation, num_rows=4, num_columns=4):
    a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    for i in a:
        print(*[f"{x:>3}" for x in i])


print_operation_table(lambda x, y: x ** y)