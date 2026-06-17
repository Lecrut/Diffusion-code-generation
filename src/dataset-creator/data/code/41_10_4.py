def count_items(iterable):
    return sum(1 for _ in iterable)
if __name__ == '__main__':
    samples = [list(range(5)), tuple('hello'), set([10, 20]), iter(['a', 'b'])]
    results = []
    for sample in samples:
        count = count_items(sample)
        if isinstance(sample, (str, bytes)):
            type_name = "string/bytes"
        else:
            type_name = type(sample).__name__
        results.append(f"{type_name}: {count}")
    print("\n".join(results))