class ConditionChecker:
    def evaluate(self, parameters):
        if not parameters:
            return False
        for key, required_value in parameters.items():
            if parameters.get(key) != required_value:
                return False
        return True
if __name__ == '__main__':
    checker = ConditionChecker()
    sample1 = {"age": 30, "is_adult": True}
    result1 = checker.evaluate(sample1)
    print(f"Sample 1 result: {result1}")
    sample2 = {"age": 30, "is_adult": False}
    result2 = checker.evaluate(sample2)
    print(f"Sample 2 result: {result2}")
    sample3 = {"age": 30, "is_adult": True, "city": "New York"}
    result3 = checker.evaluate(sample3)
    print(f"Sample 3 result: {result3}")
    sample4 = {}
    result4 = checker.evaluate(sample4)
    print(f"Sample 4 result: {result4}")
    sample5 = {"age": 31}
    result5 = checker.evaluate(sample5)
    print(f"Sample 5 result: {result5}")