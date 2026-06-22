class RangeChecker:
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val

    def check_range(self, lst):
        return all(self.min_val <= x <= self.max_val for x in lst)

if __name__ == '__main__':
    checker = RangeChecker(2, 10)
    sample_list = [3, 5, 7, 9]
    result = checker.check_range(sample_list)
    print(result)