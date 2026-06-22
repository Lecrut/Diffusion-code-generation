import random

def is_even(number):
    return number % 2 == 0

def print_number_status(number):
    if is_even(number):
        print('Even')
    else:
        print('Odd')

if __name__ == '__main__':
    for _ in range(10):
        random_number = random.randint(1, 100)
        print_number_status(random_number)