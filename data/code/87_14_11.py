def evaluate_flags(flag_x: bool, flag_y: bool) -> bool:
    return flag_x ^ flag_y

if __name__ == '__main__':
    test_cases = [
        (True, False),
        (False, True),
        (True, True),
        (False, False)
    ]

    for case in test_cases:
        result = evaluate_flags(*case)
        print(f"Test with ({case[0]}, {case[1]}): {result}")