class EqualityChecker:
    @staticmethod
    def are_values_equal(a, b):
        return a == b

if __name__ == '__main__':
    print(EqualityChecker.are_values_equal(10, 10))
    print(EqualityChecker.are_values_equal("hello", "hello"))
    print(EqualityChecker.are_values_equal([1, 2], [1, 2]))
    print(EqualityChecker.are_values_equal({"a": 1}, {"a": 1}))