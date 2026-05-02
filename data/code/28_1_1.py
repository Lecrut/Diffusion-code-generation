class ComparisonUtils:
    @staticmethod
    def check_if_greater(a, b):
        if a > b:
            return True
        else:
            return False
if __name__ == '__main__':
    num1 = 10
    num2 = 5
    result1 = ComparisonUtils.check_if_greater(num1, num2)
    print(f"Is {num1} greater than {num2}? {result1}")
    num3 = 3
    num4 = 8
    result2 = ComparisonUtils.check_if_greater(num3, num4)
    print(f"Is {num3} greater than {num4}? {result2}")
    num5 = 7
    num6 = 7
    result3 = ComparisonUtils.check_if_greater(num5, num6)
    print(f"Is {num5} greater than {num6}? {result3}")