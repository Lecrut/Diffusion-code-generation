class ValueChecker:
    def is_equal(self, value1, value2):
        return value1 == value2
if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.is_equal(10, 10))
    print(checker.is_equal(5.5, 5.5))
    print(checker.is_equal("hello", "hello"))
    print(checker.is_equal(1, 2))
    print(checker.is_equal(True, True))
    print(checker.is_equal(3.14, 3.1400000000000004))