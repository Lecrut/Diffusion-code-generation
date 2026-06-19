def sum_generator(a, b):
    yield a + b

if __name__ == '__main__':
    result = sum_generator(3, 5)
    print(next(result))