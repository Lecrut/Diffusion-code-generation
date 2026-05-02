class ComparisonUtils:
    @staticmethod
    def check_if_greater(a, b):
        if a > b:
            return True
        else:
            return False
if __name__ == '__main__':
    result1 = ComparisonUtils.check_if_greater(10, 5)
    print(f"10 > 5 is: {result1}")
    result2 = ComparisonUtils.check_if_greater(3, 8)
    print(f"3 > 8 is: {result2}")
    result3 = ComparisonUtils.check_if_greater(7, 7)
    print(f"7 > 7 is: {result3}")