class ComparisonUtils:
    @classmethod
    def check_if_greater(cls, a, b):
        return a > b

if __name__ == '__main__':
    result = ComparisonUtils.check_if_greater(10, 5)
    print(result)