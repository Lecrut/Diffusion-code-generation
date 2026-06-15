class ValueChecker:
    def check_equality(self, val1: object, val2: object) -> bool:
        return val1 == val2
if __name__ == '__main__':
    checker = ValueChecker()
    result1 = checker.check_equality(10, 10)
    print(f"10 and 10 are equal: {result1}")
    result2 = checker.check_equality("hello", "hello")
    print(f"'hello' and 'hello' are equal: {result2}")
    result3 = checker.check_equality(5, 6)
    print(f"5 and 6 are equal: {result3}")
    result4 = checker.check_equality(3.14, 3.1400000000000004)
    print(f"3.14 and 3.1400000000000004 are equal: {result4}")