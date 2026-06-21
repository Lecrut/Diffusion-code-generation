def int_generator():
    yield 10
    yield 20
    yield 30

if __name__ == '__main__':
    gen = int_generator()
    print(next(gen))