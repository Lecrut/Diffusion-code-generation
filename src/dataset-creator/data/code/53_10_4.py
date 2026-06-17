def count_items(iterable):
    return sum(1 for _ in iterable)
if __name__ == '__main__':
    test_cases = [
        [],
        [1, 2, 3],
        "hello",
        (4, 5),
        {6: 'a', 7: 'b'}
    ]
    for i, data in enumerate(test_cases):
        count = count_items(data)
        print(f"Input type: {type(data).__name__}, Count: {count}")