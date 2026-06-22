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
    print(checker.are_equal(1, 1))
    print(checker.are_equal('1', 1))
    print(checker.are_equal([1], (1,)))
    print(checker.are_equal({'a': 1}, {'a': 1}))