class ComplexConditionEvaluator:
    REQUIRED_CHAR = '1'

    @staticmethod
    def all_chars_match_required(string, required_char):
        return all(char == required_char for char in string)

    @staticmethod
    def check_and_operation(binary_string):
        if not binary_string:
            return False
        return ComplexConditionEvaluator.all_chars_match_required(binary_string, ComplexConditionEvaluator.REQUIRED_CHAR)

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
        result = ComplexConditionEvaluator.check_and_operation(input_str)
        print(f"Input: '{input_str}', Expected: {expected}, Result: {result}")