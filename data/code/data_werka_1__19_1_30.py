class ConditionChecker:

    def __init__(self):
        self.default_value = 0

    @staticmethod
    def check_condition(a, b):
        return a == b
if __name__ == '__main__':
    checker = ConditionChecker()
    print(checker.check_condition(10, 10))
    print(checker.check_condition(5, 3))
    print(checker.check_condition(0, 0))
    print(checker.check_condition(-1, -1))
    print(checker.check_condition(100, 200))