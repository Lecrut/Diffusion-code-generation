import random
RANDOM_NUMBER_RANGE = 100

def even_odd_generator(start, end):
    for _ in range(start, end + 1):
        number = random.randint(0, RANDOM_NUMBER_RANGE)
        yield (number % 2 == 0)
if __name__ == '__main__':
    start_range = 3
    end_range = 8
    generator = even_odd_generator(start_range, end_range)
    for result in generator:
        print(result)