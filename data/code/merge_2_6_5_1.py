def compare_values(a: any, b: any) -> int:
    is_none_a = (a is None)
    is_none_b = (b is None)
    if is_none_a and not is_none_b:
        return -1
    if not is_none_a and is_none_b:
        return 1
    if is_none_a and is_none_b:
        return 0
    try:
        result = a > b
        if result:
            return 1
        elif not (a < b):
            return 0
        else:
            return -1
    except TypeError:
        return 0
if __name__ == '__main__':
    test_cases = [
        (None, None),
        (5, None),
        (None, 10),
        ("apple", "banana"),
        ("zebra", "ant"),
        (3.14, 2.71),
        ([], []),
        ([], [1]),
    ]
    for a, b in test_cases:
        result = compare_values(a, b)
        print(f"compare({a!r}, {b!r}) -> {result}")