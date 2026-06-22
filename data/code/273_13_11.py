import random

def check_even_odd():
    for _ in range(10):
        num = random.randint(1, 100)
        if num % 2 == 0:
            print('Even')
        else:
            print('Odd')

if __name__ == '__main__':
    check_even_odd()