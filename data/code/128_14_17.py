class NegativeChecker:

    @staticmethod
    def is_negative(value):
        return value < 0
if __name__ == '__main__':
    test_cases = [-1.5, 2, -3, 4, -5.5]
    expected_results = [True, False, True, False, True]
    for i, test_case in enumerate(test_cases):
        result = NegativeChecker.is_negative(test_case)
        assert result == expected_results[i], f'Test {i + 1} Failed: Expected {expected_results[i]}, Got {result}'
        print(f'Test {i + 1} Passed')