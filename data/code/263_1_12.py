class RangeChecker:

    @staticmethod
    def is_within_range(value, lower_bound, upper_bound):
        return lower_bound <= value <= upper_bound
if __name__ == '__main__':
    print(RangeChecker.is_within_range(5, 1, 10))
    print(RangeChecker.is_within_range(0, -5, 5))
    print(RangeChecker.is_within_range(11, 1, 10))