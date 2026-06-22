import random

def check_even_odd():
    number = random.randint(1, 100)
    return 'Even' if number % 2 == 0 else 'Odd'

if __name__ == '__main__':
    for _ in range(10):
        print(check_even_odd())