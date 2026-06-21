class ValueChecker:

    def are_equal(self, a, b):
        if self._are_directly_comparable(a, b):
            return a == b
        elif self._can_convert_to_float(a) and self._can_convert_to_float(b):
            return float(a) == float(b)
        else:
            raise ValueError('Unsupported types for comparison')

    def _are_directly_comparable(self, a, b):
        try:
            return type(a) == type(b) or (isinstance(a, str) and isinstance(b, list)) or (isinstance(a, list) and isinstance(b, str))
        except Exception:
            return False

    def _can_convert_to_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False
if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.are_equal(10, '10'))
    print(checker.are_equal(3.14, 3.14))
    print(checker.are_equal('hello', 'world'))
    print(checker.are_equal([1, 2], [1, 2]))
    print(checker.are_equal({'a': 1}, {'a': 1}))