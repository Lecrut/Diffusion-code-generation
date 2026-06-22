class ValueChecker:

    def are_equal(self, a, b):
        if type(a) != type(b):
            try:
                a = self._convert_to_common_type(a, b)
                b = self._convert_to_common_type(b, a)
            except ValueError as e:
                return False
        return a == b

    def _convert_to_common_type(self, value, other_value):
        if isinstance(value, (int, float)) and isinstance(other_value, (int, float)):
            return float(value) if isinstance(other_value, float) else int(value)
        elif isinstance(value, str) and isinstance(other_value, (int, float)):
            try:
                return type(other_value)(value)
            except ValueError:
                raise ValueError(f'Cannot convert {value} to {type(other_value)}')
        elif isinstance(value, (int, float)) and isinstance(other_value, str):
            try:
                return type(value)(other_value)
            except ValueError:
                raise ValueError(f'Cannot convert {other_value} to {type(value)}')
        else:
            raise ValueError(f'Unsupported types for comparison: {type(a)}, {type(b)}')
if __name__ == '__main__':
    checker = ValueChecker()
    print(checker.are_equal(5, 5.0))
    print(checker.are_equal('10', 10))
    print(checker.are_equal('abc', 'def'))
    print(checker.are_equal(3.14, '3.14'))
    print(checker.are_equal([1, 2], [1, 2]))