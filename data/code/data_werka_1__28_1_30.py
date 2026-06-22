class ComparisonUtils:
    @classmethod
    def check_if_greater(cls, first, second):
        return first > second

if __name__ == '__main__':
    sample_first = 10
    sample_second = 5
    result = ComparisonUtils.check_if_greater(sample_first, sample_second)
    print(result)