class ConditionChecker:
    def __init__(self):
        self.lower_bound = 10
        self.upper_bound = 200
        self.divisor = 7

    def check_all(self, value):
        if value <= self.lower_bound:
            return False
        if value >= self.upper_bound:
            return False
        if value % self.divisor != 0:
            return False
        return value % 2 != 0

if __name__ == '__main__':
    checker = ConditionChecker()
    print(checker.check_all(14))
    print(checker.check_all(21))
    print(checker.check_all(7))