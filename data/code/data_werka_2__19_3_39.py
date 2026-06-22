import random

def even_odd_generator(start, end):
    for _ in range(start, end + 1):
        number = random.randint(0, 99)
        is_even = (number % 2 == 0)
        yield is_even

if __name__ == '__main__':
    start_range = 3
    end_range = 8
    generator = even_odd_generator(start_range, end_range)
    for result in generator:
        print(result)