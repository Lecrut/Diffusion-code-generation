def compare_pairs(iterable):
    for i in range(len(iterable) - 1):
        yield iterable[i] == iterable[i+1]
if __name__ == '__main__':
    data = [True, False, True, True, False]
    generator = compare_pairs(data)
    results = list(generator)
    print(results)