class ComparisonUtils:
    @staticmethod
    def check_if_greater(a, b):
        if a > b:
            return True
        else:
            return False
if __name__ == '__main__':
    val1 = 10
    val2 = 5
    result1 = ComparisonUtils.check_if_greater(val1, val2)
    print(f"Is {val1} greater than {val2}? {result1}")
    val3 = 3
    val4 = 7
    result2 = ComparisonUtils.check_if_greater(val3, val4)
    print(f"Is {val3} greater than {val4}? {result2}")
    val5 = 10
    val6 = 10
    result3 = ComparisonUtils.check_if_greater(val5, val6)
    print(f"Is {val5} greater than {val6}? {result3}")