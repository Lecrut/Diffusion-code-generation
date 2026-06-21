class EvenRangeChecker:
    def __init__(self, lower_bound=0, upper_bound=100):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def is_valid(self, value):
        return value > self.lower_bound and value < self.upper_bound and value % 2 == 0

if __name__ == '__main__':
    checker = EvenRangeChecker()
    print(checker.is_valid(42))
    print(checker.is_valid(99))
    print(checker.is_valid(0))