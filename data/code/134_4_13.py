def validate_exclusive_flags(flags):
    if not isinstance(flags, list) or not all(isinstance(f, int) for f in flags):
        raise ValueError("Input must be a list of integers.")
    
    total = 0
    for flag in flags:
        if flag < 0:
            raise ValueError("Flag values must be non-negative.")
        total |= flag
    
    return total == 1

if __name__ == '__main__':
    test_cases = [
        ([0], True),
        ([1], True),
        ([2], False),
        ([1, 0], True),
        ([0, 1], True),
        ([1, 1], False),
        ([0, 0], True),
        ([2, 4], False),
        ([8], True)
    ]
    
    for case in test_cases:
        print(f"validate_exclusive_flags({case[0]}) = {validate_exclusive_flags(case[0])}")