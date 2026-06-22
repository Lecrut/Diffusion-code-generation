class RangeChecker:
    MIN_RANGE = -1000
    MAX_RANGE = 1000

    @staticmethod
    def is_within_range(value):
        return RangeChecker.MIN_RANGE <= value <= RangeChecker.MAX_RANGE

    @classmethod
    def check_all_in_range(cls, lst):
        return all(cls.is_within_range(x) for x in lst)

if __name__ == '__main__':
    sample_list = [10, 20, 30, -50, 1500]
    result = RangeChecker.check_all_in_range(sample_list)
    print(result)