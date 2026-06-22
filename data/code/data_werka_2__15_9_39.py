class ValueChecker:

    def are_equal(self, a, b):
        if self._direct_compare(a, b):
            return True
        elif self._convert_and_compare(a, b):
            return True
        else:
            return False

    def _direct_compare(self, a, b):
        try:
            return a == b
        except TypeError:
            return False

    def _convert_and_compare(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, str):
            try:
                num_b = float(b)
                return a == num_b
            except ValueError:
                return False
        elif isinstance(a, str) and isinstance(b, (int, float)):
            try:
                num_a = float(a)
                return num_a == b
            except ValueError:
                return False
        else:
            return False
if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.are_equal(10, '10'))
    print(checker.are_equal(3.14, 3.14))
    print(checker.are_equal('hello', 'world'))
    print(checker.are_equal([1, 2], [1, 2]))
    print(checker.are_equal({'a': 1}, {'a': 1}))
    print(checker.are_equal(5.0, '5'))
    print(checker.are_equal('100', 100))
    print(checker.are_equal([1, 2], (1, 2)))
    print(checker.are_equal('abc', ['a', 'b', 'c']))