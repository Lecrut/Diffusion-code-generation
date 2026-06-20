def validate_exclusive_flags(flags):
    if not isinstance(flags, list) or not all(isinstance(flag, int) for flag in flags):
        raise ValueError("Input must be a list of integers.")
    
    total = 0
    for flag in flags:
        if flag < 0:
            raise ValueError("Flags must be non-negative.")
        total |= flag
    
    return total == 1 << flags.index(total) if total else False

if __name__ == '__main__':
    test_cases = [
        ([0], True),
        ([1], True),
        ([2], False),
        ([3], False),
        ([4], False),
        ([8], True),
        ([16], True),
        ([32], False),
        ([64], False),
        ([1, 2], False),
        ([2, 1], False),
        ([1, 4], True),
        ([4, 1], True),
        ([1, 8], True),
        ([8, 1], True),
        ([1, 16], True),
        ([16, 1], True),
        ([1, 32], False),
        ([32, 1], False),
        ([1, 64], False),
        ([64, 1], False),
    ]
    
    for flags in test_cases:
        print(f"validate_exclusive_flags({flags}) = {validate_exclusive_flags(flags)}")