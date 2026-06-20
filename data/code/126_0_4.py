class EqualityChecker:
    def is_equal(self, a, b):
        return a == b

if __name__ == '__main__':
    checker = EqualityChecker()
    print(checker.is_equal(5, 5))
    print(checker.is_equal(10, 5))
    print(checker.is_equal("hello", "hello"))
    print(checker.is_equal(1, 2))