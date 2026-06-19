class ComparisonUtils:
    @staticmethod
    def check_if_greater(value1, value2):
        return value1 > value2

if __name__ == '__main__':
    sample_value1 = 42
    sample_value2 = 24
    result = ComparisonUtils.check_if_greater(sample_value1, sample_value2)
    print(result)