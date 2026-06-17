def compare_adjacent(iterable):
    for i in range(len(iterable) - 1):
        yield iterable[i+1] > iterable[i]
if __name__ == '__main__':
    data = [1, 3, 2, 5, 4]
    results = list(compare_adjacent(data))
    print(results)