class ComparisonUtils:

    @staticmethod
    def check_if_greater(a, b):
        return a > b
if __name__ == '__main__':
    result = ComparisonUtils.check_if_greater(10, 5)
    print(result)
    result = ComparisonUtils.check_if_greater(3, 7)
    print(result)