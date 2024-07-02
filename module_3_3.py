# Распаковка позиционных параметров

# 1.Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print('1.Функция с параметрами по умолчанию:')
print_params(22, 33, 44)
print_params("Первый", True)
print_params("Первая", c="записана")
print_params('"2>1 "')
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

print('2.Распаковка параметров:')
values_list = ["First", 1, True]
values_dict = {'a': 'один', 'b': 'два', 'c': 'три'}
print_params(*values_list)
print_params(**values_dict)

print('3.Распаковка + отдельные параметры:')
values_list_2=[[123,234],"LIST"]
print_params(*values_list_2, 42)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)