import random

def check_even_odd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

if __name__ == '__main__':
    for _ in range(10):
        number = random.randint(1, 100)
        result = check_even_odd(number)
        print(result)