class ConditionChecker:
    def evaluate(self, parameters):
        if not parameters:
            return False
        for key, condition in parameters.items():
            if not condition:
                return False
        return True
if __name__ == '__main__':
    checker = ConditionChecker()
    test_case_1 = {"a": True, "b": 10}
    result_1 = checker.evaluate(test_case_1)
    print(f"Test Case 1 Result: {result_1}")
    test_case_2 = {"a": True, "b": False}
    result_2 = checker.evaluate(test_case_2)
    print(f"Test Case 2 Result: {result_2}")
    test_case_3 = {}
    result_3 = checker.evaluate(test_case_3)
    print(f"Test Case 3 Result: {result_3}")
    test_case_4 = {"x": 5, "y": 10}
    result_4 = checker.evaluate(test_case_4)
    print(f"Test Case 4 Result: {result_4}")