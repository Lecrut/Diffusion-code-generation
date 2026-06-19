class ComparisonUtils:
    @staticmethod
    def check_if_greater(a, b):
        return a > b

if __name__ == '__main__':
    sample_a = 10
    sample_b = 5
    result = ComparisonUtils.check_if_greater(sample_a, sample_b)
    print(result)