# calculator

'''
План:
1. ввод данных(число, его система, и нужная система)
2.Т.к. в из 10 системы можно перевести в любую системы путем деления на основание системы, переводим число в 10 
3. Создаем функцию для перевода числа в 10 систему. Чтобы перевести любое число из любой системы в 10-ную нужно полученное число
разбить на цифры, из которых состоит число, а затем каждую цифру умножать на основание этого числа в степени n1 == 0, n += 1.
4. Из полученного числа переводим в любую нужную нам систему путем деления числа на основание системы нужного числа, и ответы записываем 
с конца.
5. Profit!
'''
alpha = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c',
'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def letter_to_number(letter):
    letter = str(letter)
    for i in range(len(alpha)):
        if alpha[i] == letter.lower():
            return alpha.index(alpha[i])

def transfer_from_ten(num, base_need):
    new_num =''
    while num > 0:
        new_num += str(num % base_need)
        num //= base_need
    return int(new_num[::-1])

def transfer_in_ten(num, base_num):
    num = list(num)
    new_num = 0
    for number in range(len(num)):
        num[number] = letter_to_number(num[number])
        new_num += num[number] * base_num**((len(num)-1) - number)
    num = ''.join(map(str, num))
    num = int(num)
    return int(new_num)

num = input('Введите число: ')
while not num.isalnum():
    num = input('Число введено некорректно, попробуйте снова:')
base_num = input('Введите основание числа: ')
while not base_num.isdigit() or base_num <= 1:
    base_num = input('Основание введено некорректно, попробуйте снова:')
base_num = int(base_num)
base_need = input('Введите основание, в которое требуется перевести: ')
while not base_need.isdigit() or int(base_need) <= 1:
    base_need = input('Основание введено некорректно, попробуйте снова:')
base_need = int(base_need)
print(transfer_from_ten(transfer_in_ten(num, base_num), base_need))
