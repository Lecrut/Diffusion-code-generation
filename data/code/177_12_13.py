class StringUtils:
    @staticmethod
    def split_string_by_space(input_string):
        return input_string.split()

if __name__ == '__main__':
    test_strings = [
        ("this is a sample string", ["this", "is", "a", "sample", "string"]),
        ("  leading and trailing spaces   in between ", ["leading", "and", "trailing", "spaces", "in", "between"]),
        ("singleword", ["singleword"]),
        ("", [])
    ]

    for test_string, expected in test_strings:
        result = StringUtils.split_string_by_space(test_string)
        print(f"Input: '{test_string}'")
        print(f"Expected Output: {expected}")
        print(f"Actual Output: {result}")
        print()