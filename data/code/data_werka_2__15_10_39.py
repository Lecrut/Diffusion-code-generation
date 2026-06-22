class EqualityChecker:
    @staticmethod
    def are_equal(a, b):
        return a == b

if __name__ == '__main__':
    print(EqualityChecker.are_equal(10, 10))  # True
    print(EqualityChecker.are_equal("hello", "world"))  # False
    print(EqualityChecker.are_equal([1, 2, 3], [1, 2, 3]))  # True
    print(EqualityChecker.are_equal({"a": 1}, {"a": 1}))  # True