class ComparisonUtils:
    @staticmethod
    def check_if_greater(a, b):
        return a > b

if __name__ == '__main__':
    utils = ComparisonUtils()
    result = utils.check_if_greater(10, 5)
    print(result)