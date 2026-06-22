class ComparisonUtils:

    def check_greater(self, val1, val2):
        return val1 > val2
if __name__ == '__main__':
    comparison_utils = ComparisonUtils()
    result = comparison_utils.check_greater(10, 5)
    print(result)
    result = comparison_utils.check_greater(3, 7)
    print(result)