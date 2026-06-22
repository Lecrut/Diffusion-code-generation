class ComparisonUtils:
    def check_greater(self, val1, val2):
        return val1 > val2

if __name__ == '__main__':
    cu = ComparisonUtils()
    result = cu.check_greater(10, 5)
    print(result)