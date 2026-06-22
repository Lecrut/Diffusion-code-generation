import random

def check_even_odd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

def repeat_check_even_odd(count):
    for _ in range(count):
        number = random.randint(1, 100)
        result = check_even_odd(number)
        print(result)

if __name__ == '__main__':
    sample_count = 10
    repeat_check_even_odd(sample_count)