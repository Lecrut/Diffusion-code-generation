import random

def check_even_odd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

if __name__ == '__main__':
    sample_numbers = [42, 17, 83, 56, 99, 21, 64, 33, 72, 100]
    for number in sample_numbers:
        result = check_even_odd(number)
        print(f'{number}: {result}')