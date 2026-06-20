def validate_exclusive_flags(flags):
    if not isinstance(flags, list) or not all(isinstance(flag, int) for flag in flags):
        raise ValueError("Input must be a list of integers.")
    
    combined = sum(flags)
    return combined == 1

if __name__ == '__main__':
    test_cases = [
        ([0, 0, 0], True),
        ([1, 0, 0], True),
        ([0, 1, 0], True),
        ([1, 1, 0], False),
        ([1, 0, 1], False),
        ([0, 0], True),
        ([1], True),
        ([], True)
    ]
    
    for i, test_case in enumerate(test_cases):
        print(f"Test case {i+1}: Input = {test_case[0]}, Expected = {test_case[1]}, Result = {validate_exclusive_flags(test_case[0])}")