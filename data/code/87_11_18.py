class ConditionChecker:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def check_conditions(self):
        return self.x > 5 and self.y < 10

if __name__ == '__main__':
    checker = ConditionChecker(6, 8)
    result = checker.check_conditions()
    print(result)