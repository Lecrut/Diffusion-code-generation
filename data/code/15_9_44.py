class ValueChecker:

    def are_equal(self, a, b):
        try:
            return a == b
        except TypeError:
            return str(a) == str(b)
if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.are_equal(1, 1))
    print(checker.are_equal('1', 1))
    print(checker.are_equal([1, 2], [1, 2]))
    print(checker.are_equal([1, 2], (1, 2)))
    print(checker.are_equal(None, None))
    print(checker.are_equal(True, 1))