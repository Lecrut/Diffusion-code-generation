def count_items(iterable):
    return sum(1 for _ in iterable)
if __name__ == '__main__':
    test_cases = [(), [], {}, set(), "hello", range(5), []]
    results = {}
    for i, item in enumerate(test_cases):
        count = count_items(item)
        results[i] = count
    print("Count Results:")
    for idx, val in results.items():
        if isinstance(val, int):
            print(f"Index {idx}: Count is {val}")