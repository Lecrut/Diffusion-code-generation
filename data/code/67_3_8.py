def sum_generator(a, b):
    yield a + b

if __name__ == '__main__':
    numbers = {'first': 3, 'second': 7}
    result = next(sum_generator(numbers['first'], numbers['second']))
    print(result)