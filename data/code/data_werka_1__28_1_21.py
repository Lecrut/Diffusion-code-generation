class ComparisonUtils:

    @staticmethod
    def check_if_greater(value1, value2):
        return value1 > value2
if __name__ == '__main__':
    result = ComparisonUtils.check_if_greater(10, 5)
    print(result)
    result = ComparisonUtils.check_if_greater(3, 8)
    print(result)