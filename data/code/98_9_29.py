class ConditionChecker:
    MIN_VALUE = 0
    MAX_VALUE = 100
    DIVISOR_2 = 2
    DIVISOR_3 = 3
    EXACT_VALUE = 50

    def __init__(self):
        self.conditions = [
            lambda x: x > self.MIN_VALUE,
            lambda x: x < self.MAX_VALUE,
            lambda x: x % self.DIVISOR_2 == 0,
            lambda x: x % self.DIVISOR_3 == 0,
            lambda x: x != self.EXACT_VALUE
        ]

    def check_all(self, value):
        for condition in self.conditions:
            if not condition(value):
                return False
        return True

if __name__ == '__main__':
    checker = ConditionChecker()
    print(checker.check_all(12))
    print(checker.check_all(50))
    print(checker.check_all(100))
    print(checker.check_all(-5))
    print(checker.check_all(13))