def get_nth(generator, n):
    iterator = iter(generator)
    for _ in range(n):
        next(iterator)
    return next(iterator)
if __name__ == '__main__':

    def sample_generator():
        for i in range(100):
            yield i
    result = get_nth(sample_generator(), 10)
    print(result)