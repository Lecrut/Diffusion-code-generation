class ValueChecker:
    @staticmethod
    def are_equal(a, b):
        return a == b
if __name__ == '__main__':
    val1 = 10
    val2 = 10
    val3 = "hello"
    val4 = "world"
    print(f"Are {val1} and {val2} equal? {ValueChecker.are_equal(val1, val2)}")
    print(f"Are {val3} and {val4} equal? {ValueChecker.are_equal(val3, val4)}")