class LogicalConditionChecker:
    @staticmethod
    def is_valid_number(value):
        return value.isdigit() and all(char == '1' for char in value)

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
    
    checker = LogicalConditionChecker()
    for input_str, expected in test_cases:
        result = checker.is_valid_number(input_str)
        print(f"Input: {input_str}, Expected: {expected}, Result: {result}")