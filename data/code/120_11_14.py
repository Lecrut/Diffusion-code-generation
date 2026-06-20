class EqualityChecker:
    @staticmethod
    def are_equal(a, b):
        return a == b

if __name__ == '__main__':
    checker = EqualityChecker()
    print(checker.are_equal(1, 2))
    print(checker.are_equal('hello', 'hello'))
    print(checker.are_equal([1, 2], [1, 2]))
    print(checker.are_equal({'a': 1}, {'a': 1}))
    print(checker.are_equal((1, 2), (1, 2)))
    print(checker.are_equal(True, True))
    print(checker.are_equal(False, False))
    print(checker.are_equal(None, None))