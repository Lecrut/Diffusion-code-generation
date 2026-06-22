import random

def check_even_odd():
    even_odd = {True: 'Even', False: 'Odd'}
    number = random.randint(1, 100)
    print(even_odd[number % 2 == 0])

if __name__ == '__main__':
    for _ in range(10):
        check_even_odd()