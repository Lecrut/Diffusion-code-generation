def count_items(iterable):
    return sum(1 for _ in iterable)
if __name__ == '__main__':
    samples = [list(range(5)), tuple('hello'), set([10, 20]), iter(['a', 'b'])]
    results = []
    for sample in samples:
        count = count_items(sample)
        results.append((type(sample).__name__, len(list(sample))))
    print(results)