def sum_generator(a, b):
    yield a + b
if __name__ == '__main__':
    gen = sum_generator(5, 3)
    print(next(gen))
    gen = sum_generator(10, 20)
    print(next(gen))
    gen = sum_generator(1, 1)
    print(next(gen))