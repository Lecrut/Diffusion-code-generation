def get_nth_element(generator, n):
    iterator = iter(generator)
    for _ in range(n):
        next(iterator)
    return next(iterator)

if __name__ == '__main__':
    def count():
        i = 0
        while True:
            yield i
            i += 1

    result = get_nth_element(count(), 5)
    print(result)