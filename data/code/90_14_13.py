class OrConditionTester:
    TEST_CASES = [
        (0, 1),
        (None, "hello"),
        (False, True),
        ([], [1, 2]),
        ("", "world"),
        (0, 0),
        (None, None),
        (False, False)
    ]

    @staticmethod
    def _is_valid_operand(operand):
        return isinstance(operand, (int, float, str, bool, type(None), list, dict, tuple))

    @staticmethod
    def evaluate(a, b):
        if not OrConditionTester._is_valid_operand(a):
            raise ValueError("Left operand must be a valid Python object")
        if not OrConditionTester._is_valid_operand(b):
            raise ValueError("Right operand must be a valid Python object")
        return a or b

if __name__ == '__main__':
    tester = OrConditionTester()
    for left, right in tester.TEST_CASES:
        result = tester.evaluate(left, right)
        print(result)