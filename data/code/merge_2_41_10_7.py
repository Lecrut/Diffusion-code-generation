def count_items(iterable):
    if not hasattr(iterable, "__iter__"):
        raise TypeError("Input must be iterable")
    return sum(1 for _ in iterable)
if __name__ == '__main__':
    samples = [
        [],
        (1,),
        {2},
        range(3),
        "hello"
    ]
    results = []
    for sample in samples:
        count = count_items(sample)
        results.append((type(sample).__name__, len(sample)))
    print(results)