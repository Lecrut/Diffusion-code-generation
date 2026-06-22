def number_generator():
    yield 42
    yield 100
    yield 200

if __name__ == '__main__':
    gen = number_generator()
    print(next(gen))