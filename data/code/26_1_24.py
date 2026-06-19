class ComparisonUtils:

    def check_greater(self, val1, val2):
        return val1 > val2
if __name__ == '__main__':
    comp_utils = ComparisonUtils()
    print(comp_utils.check_greater(10, 5))
    print(comp_utils.check_greater(3, 8))