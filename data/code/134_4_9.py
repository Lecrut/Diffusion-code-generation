def validate_exclusive_flags(flags):
    combined = 0
    for flag in flags:
        if flag:
            combined |= 1 << (combined.bit_count())
    return combined == 0

if __name__ == '__main__':
    test_cases = [
        ([1, 0, 0], True),
        ([0, 2, 0], True),
        ([0, 0, 4], True),
        ([8, 0, 0], True),
        ([16, 32, 0], False),
        ([0, 0], True),
        ([1], True),
        ([], True),
        ([1, 2], False)
    ]
    for flags in test_cases:
        print(validate_exclusive_flags(flags))