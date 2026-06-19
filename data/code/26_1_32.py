class ComparisonUtils:

    def check_greater(self, val1, val2):
        return val1 > val2
if __name__ == '__main__':
    cu = ComparisonUtils()
    print(cu.check_greater(10, 5))
    print(cu.check_greater(3, 7))
    print(cu.check_greater(0, 0))