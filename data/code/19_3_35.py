import random

def even_odd_generator(start, end):
    for _ in range(start, end + 1):
        num = random.randint(1, 100)
        yield num % 2 == 0

if __name__ == '__main__':
    start_range = 5
    end_range = 10
    generator = even_odd_generator(start_range, end_range)
    for result in generator:
        print(result)