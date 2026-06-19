import random

def even_odd_generator(start, end):
    for _ in range(start, end + 1):
        number = random.randint(0, 9)
        yield number % 2 == 0

if __name__ == '__main__':
    start_range = 5
    end_range = 10
    generator = even_odd_generator(start_range, end_range)
    for result in generator:
        print(result)