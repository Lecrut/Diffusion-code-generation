class OrConditionTester:
    TEST_CASES = [
        (True, True, True),
        (True, False, True),
        (False, True, True),
        (False, False, False)
    ]

    @staticmethod
    def test_or_condition(a, b):
        return a or b

    @classmethod
    def run_tests(cls):
        all_passed = True
        for a, b, expected in cls.TEST_CASES:
            result = cls.test_or_condition(a, b)
            if result != expected:
                print(f"Test failed for a={a}, b={b}. Expected: {expected}, Got: {result}")
                all_passed = False
        return all_passed

if __name__ == '__main__':
    test_results = OrConditionTester.run_tests()
    print("All tests passed:", test_results)