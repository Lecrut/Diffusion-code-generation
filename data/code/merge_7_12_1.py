class ValueChecker:
    @staticmethod
    def are_equal(a, b):
        return a == b
if __name__ == '__main__':
    val1 = 10
    val2 = 10
    val3 = 5
    val4 = 6.0
    val5 = 6
    print(f"10 == 10: {ValueChecker.are_equal(val1, val2)}")
    print(f"5 == 10: {ValueChecker.are_equal(val3, val1)}")
    print(f"6.0 == 6: {ValueChecker.are_equal(val4, val5)}")