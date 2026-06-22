class ConditionChecker:
    def __init__(self):
        self.conditions = [
            lambda x: x > 0,
            lambda x: x < 100,
            lambda x: x % 2 == 0,
        ]

    def check_all(self, value):
        return all(cond(value) for cond in self.conditions)

if __name__ == '__main__':
    checker = ConditionChecker()
    result = checker.check_all(50)
    print(result)