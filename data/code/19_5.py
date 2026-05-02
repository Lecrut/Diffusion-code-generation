import random
def even_odd_generator(start, end):
    for number in range(start, end + 1):
        yield number % 2 == 0
if __name__ == '__main__':
    for result in even_odd_generator(1, 10):
        print(result)