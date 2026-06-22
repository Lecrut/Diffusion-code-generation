import random

def print_even_odd():
    EVEN = 'Even'
    ODD = 'Odd'
    number = random.randint(1, 100)
    result = EVEN if number % 2 == 0 else ODD
    print(result)

if __name__ == '__main__':
    for _ in range(10):
        print_even_odd()