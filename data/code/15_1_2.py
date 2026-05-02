class ValueChecker:
    def are_equal(self, a: object, b: object) -> bool:
        return a == b
if __name__ == '__main__':
    checker = ValueChecker()
    result1 = checker.are_equal(10, 10)
    print(f"10 and 10 are equal: {result1}")
    result2 = checker.are_equal("hello", "hello")
    print(f"'hello' and 'hello' are equal: {result2}")
    result3 = checker.are_equal(5.5, 5.5)
    print(f"5.5 and 5.5 are equal: {result3}")
    result4 = checker.are_equal(1, 2)
    print(f"1 and 2 are equal: {result4}")
    result5 = checker.are_equal(True, True)
    print(f"True and True are equal: {result5}")
    result6 = checker.are_equal(10, 5)
    print(f"10 and 5 are equal: {result6}")