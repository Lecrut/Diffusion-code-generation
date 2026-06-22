class RangeChecker:

    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def is_within_range(self, number):
        return self.lower_bound <= number <= self.upper_bound
if __name__ == '__main__':
    checker = RangeChecker(10, 20)
    print(checker.is_within_range(15))
    print(checker.is_within_range(5))
    print(checker.is_within_range(25))