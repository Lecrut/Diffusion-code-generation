def check_and_operation(binary_string):
    if not binary_string:
        return False
    for char in binary_string:
        if char != '1':
            return False
    return True
if __name__ == '__main__':
    test_cases = [
        ("111", True),
        ("101", False),
        ("011", False),
        ("110", False),
        ("", False),
        ("1", True),
        ("0", False)
    ]
    for input_str, expected in test_cases:
        result = check_and_operation(input_str)
        print(f"Input: {input_str}, Expected: {expected}, Got: {result}, Match: {result == expected}")