# Lambda to check if an integer is negative
is_negative_lambda = lambda x: x < 0

if __name__ == '__main__':
    test_cases = [
        (-5, True),
        (0, False),
        (10, False),
        (-1, True),
        (-42, True)
    ]
    
    print("Testing is_negative_lambda:")
    for input_val, expected in test_cases:
        result = is_negative_lambda(input_val)
        status = "PASS" if result == expected else "FAIL"
        print(f"f({input_val}) = {result} (Expected: {expected}) - [{status}]")