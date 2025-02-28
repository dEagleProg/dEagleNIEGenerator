import random
import string

def calculate_control_letter(number):
    letters = 'TRWAGMYFPDXBNJZSQVHLCKE'
    return letters[number % 23]

def generate_nie():
    first_letter = random.choice('XYZ')
    digits = ''.join(random.choices(string.digits, k=7))
    number = int(digits)
    if first_letter == 'Y':
        number += 10000000
    elif first_letter == 'Z':
        number += 20000000
    control_letter = calculate_control_letter(number)
    return f'{first_letter}{digits}{control_letter}'

def validate_nie(nie):
    if len(nie) != 9:
        return False
    first_letter = nie[0]
    digits = nie[1:8]
    control_letter = nie[8]
    if first_letter not in 'XYZ' or not digits.isdigit() or not control_letter.isalpha():
        return False
    number = int(digits)
    if first_letter == 'Y':
        number += 10000000
    elif first_letter == 'Z':
        number += 20000000
    return calculate_control_letter(number) == control_letter

# Пример использования
new_nie = generate_nie()
print(f'Сгенерированный NIE: {new_nie}')
print(f'Проверка валидности: {validate_nie(new_nie)}')