import random

def even_odd_generator(start, end):
    for _ in range(start, end + 1):
        number = random.randint(start, end)
        yield (number % 2 == 0)

if __name__ == '__main__':
    start_range = 1
    end_range = 10
    for result in even_odd_generator(start_range, end_range):
        print(result)