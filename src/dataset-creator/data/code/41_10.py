def count_items(iterable):
    return sum(1 for _ in iterable)
if __name__ == '__main__':
    test_cases = [
        [],
        (1,),
        {2},
        iter([3]),
        ['a', 'b'],
        ('x', 'y'),
        set(),
        range(5),
    ]
    for item in test_cases:
        print(f"Count of {type(item).__name__}: {count_items(item)}")