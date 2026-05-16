class ValueChecker:
    def is_equal(self, val1, val2):
        return val1 == val2
if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.is_equal(5, 5))
    print(checker.is_equal(10, 5))
    print(checker.is_equal("hello", "hello"))
    print(checker.is_equal(3.14, 3.1400000000000004))