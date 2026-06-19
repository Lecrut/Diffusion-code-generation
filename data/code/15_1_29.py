class ValueChecker:
    def are_equal(self, a: object, b: object) -> bool:
        return a == b

if __name__ == '__main__':
    checker = ValueChecker()
    result1 = checker.are_equal(42, 42)
    result2 = checker.are_equal("hello", "world")
    print(result1)
    print(result2)