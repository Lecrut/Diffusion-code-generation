class ConditionChecker:
    def evaluate(self, parameters):
        if not parameters:
            return True
        for key, condition in parameters.items():
            if not condition:
                return False
        return True
if __name__ == '__main__':
    checker = ConditionChecker()
    sample1 = {"a": True, "b": 10}
    result1 = checker.evaluate(sample1)
    print(f"Sample 1 Result: {result1}")
    sample2 = {"a": True, "b": False}
    result2 = checker.evaluate(sample2)
    print(f"Sample 2 Result: {result2}")
    sample3 = {}
    result3 = checker.evaluate(sample3)
    print(f"Sample 3 Result: {result3}")
    sample4 = {"x": 5, "y": 10}
    result4 = checker.evaluate(sample4)
    print(f"Sample 4 Result: {result4}")