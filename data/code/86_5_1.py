def compare_pairs(iterable):
    it = iter(iterable)
    while True:
        try:
            a = next(it)
            b = next(it)
            yield a == b
        except StopIteration:
            break
if __name__ == '__main__':
    data = [True, False, True, True, False, False]
    generator = compare_pairs(data)
    results = list(generator)
    print(results)