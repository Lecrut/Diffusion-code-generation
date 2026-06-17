def count_items(iterable):
    return sum(1 for _ in iterable)
if __name__ == '__main__':
    samples = [
        [],
        (1,),
        {2},
        iter([3, 4]),
        ['a', 'b'],
        {'c'},
        tuple(),
        set()
    ]
    for sample in samples:
        print(f"Count of {type(sample).__name__}: {count_items(sample)}")