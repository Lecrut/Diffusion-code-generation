import random

def check_even_odd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

if __name__ == '__main__':
    sample_values = [1, 3, 5, 7, 9]
    for _ in range(10):
        random_number = random.randint(1, 100)
        result = check_even_odd(random_number)
        print(f'Number: {random_number}, Result: {result}')