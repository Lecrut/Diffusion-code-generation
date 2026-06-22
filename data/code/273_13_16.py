import random

def check_even_odd():
    num = random.randint(1, 100)
    if num % 2 == 0:
        print('Even')
    else:
        print('Odd')

if __name__ == '__main__':
    for _ in range(10):
        check_even_odd()