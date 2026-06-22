class ValueChecker:
    def are_equal(self, a: object, b: object) -> bool:
        return a == b

if __name__ == '__main__':
    checker = ValueChecker()
    result = checker.are_equal(42, 42)
    print(result)
    result = checker.are_equal("hello", "world")
    print(result)