def validate_exclusive_flags(flags):
    return (flags[0] & ~sum(flags[1:])) == flags[0]

if __name__ == '__main__':
    test_cases = [
        ([0, 0, 0], True),
        ([1, 0, 0], True),
        ([0, 1, 0], True),
        ([1, 1, 0], False),
        ([1, 1, 1], False),
        ([0, 0], True),
        ([1], True),
        ([], True),
        ([1, 0], False),
    ]
    for flags in test_cases:
        print(f'flags={flags} result={validate_exclusive_flags(flags)}')