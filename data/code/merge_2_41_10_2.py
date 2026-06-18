def count_items(iterable):
    return sum(1 for _ in iterable)
if __name__ == '__main__':
    test_cases = [
        [],
        (1,),
        {2},
        iter([3, 4]),
        ['a', 'b'],
        None                                                                                                                                             
    ]
    for i, case in enumerate(test_cases):
        try:
            result = count_items(case)
            print(f"Input {i}: {case!r} -> Count: {result}")
        except Exception as e:
            print(f"Input {i}: Error - {e}")