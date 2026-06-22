class ComparisonUtils:
    @classmethod
    def check_if_greater(cls, a, b):
        return a > b

if __name__ == '__main__':
    sample_value1 = 10
    sample_value2 = 5
    result = ComparisonUtils.check_if_greater(sample_value1, sample_value2)
    print(result)