class ValueChecker:
    def are_equal(self, a: object, b: object) -> bool:
        return a == b
if __name__ == '__main__':
    checker = ValueChecker()
    result1 = checker.are_equal(10, 10)
    print(f"are_equal(10, 10): {result1}")
    result2 = checker.are_equal("hello", "hello")
    print(f"are_equal(\"hello\", \"hello\"): {result2}")
    result3 = checker.are_equal(5.5, 5.5)
    print(f"are_equal(5.5, 5.5): {result3}")
    result4 = checker.are_equal(1, 2)
    print(f"are_equal(1, 2): {result4}")
    result5 = checker.are_equal(True, True)
    print(f"are_equal(True, True): {result5}")
    result6 = checker.are_equal(10, 11)
    print(f"are_equal(10, 11): {result6}")