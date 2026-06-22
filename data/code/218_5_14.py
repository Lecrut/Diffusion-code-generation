def min_value_generator():
    yield 5
    yield 3
    yield 9
    yield 1
    yield 7

if __name__ == '__main__':
    gen = min_value_generator()
    min_val = next(gen)
    for value in gen:
        if value < min_val:
            min_val = value
    print(min_val)