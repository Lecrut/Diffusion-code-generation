def min_generator():
    yield 5
    yield 3
    yield 8
    yield 1

if __name__ == '__main__':
    min_val = min(min_generator())
    print(min_val)