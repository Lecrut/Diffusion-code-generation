class ConditionChecker:
    def __init__(self, conditions):
        self.conditions = conditions
    def check_all(self, data):
        result = True
        for condition in self.conditions:
            if not condition(data):
                result = False
                break
        return result
if __name__ == '__main__':
    sample_conditions = [
        lambda x: x > 10,
        lambda x: x % 2 == 0,
        lambda x: x < 100
    ]
    checker = ConditionChecker(sample_conditions)
    test_data_1 = 50
    test_data_2 = 15
    test_data_3 = 100
    result_1 = checker.check_all(test_data_1)
    result_2 = checker.check_all(test_data_2)
    result_3 = checker.check_all(test_data_3)
    print(f"Data: {test_data_1}, Result: {result_1}")
    print(f"Data: {test_data_2}, Result: {result_2}")
    print(f"Data: {test_data_3}, Result: {result_3}")