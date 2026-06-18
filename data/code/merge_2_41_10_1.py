def count_items(iterable):
    return sum(1 for _ in iterable)
if __name__ == '__main__':
    samples = [
        [],
        (1,),
        {2},
        iter(range(3))
    ]
    results = []
    for sample in samples:
        count = count_items(sample)
        results.append((type(sample).__name__, len(list(sample)), count))
    print(results)