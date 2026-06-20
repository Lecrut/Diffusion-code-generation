class EqualityChecker:
    @staticmethod
    def is_equal(a, b):
        return a == b

if __name__ == '__main__':
    print(EqualityChecker.is_equal(5, 5))
    print(EqualityChecker.is_equal(10, 5))
    print(EqualityChecker.is_equal("hello", "hello"))
    print(EqualityChecker.is_equal(1, 2))