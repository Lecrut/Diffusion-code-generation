class RangeChecker:
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val

    def is_within_range(self, value):
        return self.min_val <= value <= self.max_val

if __name__ == '__main__':
    checker = RangeChecker(2, 10)
    sample_values = [3, 5, 7, 9]
    all_in_range = all(checker.is_within_range(x) for x in sample_values)
    print(all_in_range)