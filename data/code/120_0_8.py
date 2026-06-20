class EqualityChecker:
    @staticmethod
    def are_values_equal(a: any, b: any) -> bool:
        return a == b

if __name__ == '__main__':
    print(EqualityChecker.are_values_equal(5, 5))
    print(EqualityChecker.are_values_equal("hello", "hello"))
    print(EqualityChecker.are_values_equal([1, 2], [1, 2]))
    print(EqualityChecker.are_values_equal(3.14, 3.14))
    print(EqualityChecker.are_values_equal(True, True))
    print(EqualityChecker.are_values_equal(None, None))
    print(EqualityChecker.are_values_equal({}, {}))
    print(EqualityChecker.are_values_equal((1,), (1,)))