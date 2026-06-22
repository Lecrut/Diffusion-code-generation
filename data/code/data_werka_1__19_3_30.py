import random

def even_odd_generator(start, end):
    for _ in range(start, end + 1):
        number = random.randint(1, 100)
        yield number % 2 == 0

if __name__ == '__main__':
    start = 1
    end = 10
    generator = even_odd_generator(start, end)
    for result in generator:
        print(result)