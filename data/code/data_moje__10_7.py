def integer_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

if __name__ == '__main__':
    gen = integer_generator()
    first_value = next(gen)
    print(first_value)