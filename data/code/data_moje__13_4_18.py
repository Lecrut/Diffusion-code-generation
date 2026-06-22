def get_nth(generator, n):
    try:
        for _ in range(n):
            next(generator)
        return next(generator)
    except StopIteration:
        return None

def simple_generator():
    yield 10
    yield 20
    yield 30
    yield 40
    yield 50

if __name__ == '__main__':
    gen = simple_generator()
    result = get_nth(gen, 3)
    print(result)