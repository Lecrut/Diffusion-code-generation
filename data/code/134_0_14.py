class ConditionEvaluator:
    @staticmethod
    def are_conditions_mutually_exclusive(a: bool, b: bool, c: bool) -> bool:
        count = (a << 2) + (b << 1) + c
        return count == 1

if __name__ == '__main__':
    test_case_1 = ConditionEvaluator.are_conditions_mutually_exclusive(True, False, True)
    print(f"Test Case 1 Result: {test_case_1}")
    test_case_2 = ConditionEvaluator.are_conditions_mutually_exclusive(True, True, False)
    print(f"Test Case 2 Result: {test_case_2}")
    test_case_3 = ConditionEvaluator.are_conditions_mutually_exclusive(True, False, False)
    print(f"Test Case 3 Result: {test_case_3}")