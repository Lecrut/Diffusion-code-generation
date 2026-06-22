class ValueChecker:

    def are_equal(self, a, b):
        if type(a) != type(b):
            try:
                a = self._convert_type(a, type(b))
            except (ValueError, TypeError):
                return False
        return a == b

    def _convert_type(self, value, target_type):
        if target_type is int:
            return int(value)
        elif target_type is float:
            return float(value)
        elif target_type is str:
            return str(value)
        else:
            raise TypeError('Unsupported type conversion')
if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.are_equal(5, '5'))
    print(checker.are_equal('10.5', 10.5))
    print(checker.are_equal(True, 1))
    print(checker.are_equal([1, 2], (1, 2)))