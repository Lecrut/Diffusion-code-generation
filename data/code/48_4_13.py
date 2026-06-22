def max_generator():
    def data_points():
        yield 3.14
        yield -7
        yield 42
        yield 1.5
        yield 99
        yield -100
        yield 0

    current_max = None
    for value in data_points():
        if current_max is None or value > current_max:
            current_max = value
    yield current_max

if __name__ == '__main__':
    result = max_generator()
    print(next(result))