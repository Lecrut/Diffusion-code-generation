def count_items(iterable):
    return sum(1 for _ in iterable)
if __name__ == '__main__':
    test_cases = [
        [],
        [1, 2, 3],
        "hello",
        range(0),
        {1: 'a', 2: 'b'},
        (x ** x for x in range(5))
    ]
    results = []
    for i, data in enumerate(test_cases):
        count = count_items(data)
        results.append(f"Input type: {type(data).__name__}, Count: {count}")
    print("\n".join(results))