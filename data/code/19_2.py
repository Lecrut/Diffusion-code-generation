class ConditionChecker:
    def check_condition(self, a, b):
        return a == b
if __name__ == '__main__':
    checker = ConditionChecker()
    print(checker.check_condition(5, 5))
    print(checker.check_condition(10, 5))
    print(checker.check_condition(3.14, 3.14))
    print(checker.check_condition(1, 2))