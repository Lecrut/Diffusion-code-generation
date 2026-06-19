class ConditionChecker:

    def check_condition(self, a, b):
        return a == b
if __name__ == '__main__':
    checker = ConditionChecker()
    result = checker.check_condition(5, 5)
    print(result)
    result = checker.check_condition(3, 4)
    print(result)