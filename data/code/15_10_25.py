class ValueChecker:

    def are_equal(self, a, b):
        try:
            return a == b
        except TypeError:
            try:
                return str(a) == str(b)
            except Exception:
                return False
if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.are_equal(10, 10))
    print(checker.are_equal('10', 10))
    print(checker.are_equal([1, 2], [1, 2]))
    print(checker.are_equal((1, 2), [1, 2]))
    print(checker.are_equal({'a': 1}, {'a': 1}))
    print(checker.are_equal(None, None))
    print(checker.are_equal(True, 1))
    print(checker.are_equal('True', True))