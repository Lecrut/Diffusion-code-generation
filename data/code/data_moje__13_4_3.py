def get_nth(generator, n):
    iterator = iter(generator)
    for _ in range(n):
        next(iterator)
    return next(iterator)

if __name__ == '__main__':
    def my_generator():
        yield 10
        yield 20
        yield 30
        yield 40

    result = get_nth(my_generator(), 2)
    print(result)