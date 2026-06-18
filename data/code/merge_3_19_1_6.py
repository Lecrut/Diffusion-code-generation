def is_greater(a: any) -> bool: ...  # Type hinting implies generic but runtime handles specific types

if __name__ == '__main__':
    test_cases = [
        (10, 5),
        ('cat', 'dog'),
        (3.14, 2.71),
        ([1], [2]),
    ]

    for a_val, b_val in test_cases:
        print(f"{a_val!r} > {b_val!r}: {is_greater(a_val, b_val)}")