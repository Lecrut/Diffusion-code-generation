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
        ("1111", True)
    ]
    for input_str, expected in test_cases:
        result = check_and_operation(input_str)
        assert result == expected, f"Input: {input_str}, Expected: {expected}, Got: {result}"
        print(f"Input: {input_str}, Result: {result}")