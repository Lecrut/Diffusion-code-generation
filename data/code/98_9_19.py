class ConditionChecker:
    def __init__(self):
        self.conditions = [
            lambda x: x > 0,
            lambda x: x < 100,
            lambda x: x % 2 == 0,
            lambda x: x % 5 == 0,
        ]

    def check_all(self, value):
        return all(cond(value) for cond in self.conditions)

if __name__ == '__main__':
    checker = ConditionChecker()
    result = checker.check_all(10)
    print(result)
    result2 = checker.check_all(7)
    print(result2)
    result3 = checker.check_all(0)
    print(result3)