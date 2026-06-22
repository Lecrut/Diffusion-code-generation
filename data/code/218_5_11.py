def min_value_generator():
    yield 3
    yield 1
    yield 4
    yield 1
    yield 5

if __name__ == '__main__':
    gen = min_value_generator()
    current_min = next(gen)
    for value in gen:
        if value < current_min:
            current_min = value
    print(current_min)