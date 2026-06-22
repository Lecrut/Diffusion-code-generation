class ComparisonUtils:

    @staticmethod
    def check_if_greater(a, b):
        return a > b
if __name__ == '__main__':
    value1 = 10
    value2 = 5
    comparison_result = ComparisonUtils.check_if_greater(value1, value2)
    print(comparison_result)