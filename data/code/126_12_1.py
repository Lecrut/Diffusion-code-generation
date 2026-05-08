class ValueChecker:
    def is_equal(self, val1, val2):
        return val1 == val2
if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.is_equal(10, 10))
    print(checker.is_equal(5, 3))
    print(checker.is_equal("hello", "hello"))
    print(checker.is_equal(True, True))
    print(checker.is_equal(1.5, 1.50))