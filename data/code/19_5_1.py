import random
def even_odd_generator(start, end):
    for num in range(start, end + 1):
        yield num % 2 == 0
if __name__ == '__main__':
    generator = even_odd_generator(1, 10)
    results = list(generator)
    print(results)