def number_generator():
    yield 10
    yield 20
    yield 30

if __name__ == '__main__':
    gen = number_generator()
    first_value = next(gen)
    print(first_value)