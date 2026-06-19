class ConditionChecker:

    def check_condition(self, a, b):
        return a == b
if __name__ == '__main__':
    checker = ConditionChecker()
    value1 = 7
    value2 = 7
    result1 = checker.check_condition(value1, value2)
    print(result1)
    value3 = 45
    value4 = 90
    result2 = checker.check_condition(value3, value4)
    print(result2)
    value5 = -10
    value6 = -10
    result3 = checker.check_condition(value5, value6)
    print(result3)