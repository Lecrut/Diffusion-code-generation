class ComparisonUtils:
    def check_greater(self, val1, val2):
        return val1 > val2
if __name__ == '__main__':
    utils = ComparisonUtils()
    print(utils.check_greater(10, 5))
    print(utils.check_greater(3, 8))
    print(utils.check_greater(7, 7))
    print(utils.check_greater(-1, 0))