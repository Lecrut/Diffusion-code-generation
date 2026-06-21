class ValueChecker:

    def __init__(self):
        self.supported_types = {int, float, str}

    def _is_supported_type(self, value):
        return isinstance(value, tuple(self.supported_types))

    def are_different(self, val1, val2):
        if not self._is_supported_type(val1) or not self._is_supported_type(val2):
            raise ValueError(f'Unsupported type: {type(val1).__name__} or {type(val2).__name__}')
        return val1 != val2
if __name__ == '__main__':
    checker = ValueChecker()
    result_int = checker.are_different(10, 20)
    print('Integers different:', result_int)
    result_str = checker.are_different('hello', 'world')
    print('Strings different:', result_str)
    result_float = checker.are_different(3.14, 2.718)
    print('Floats different:', result_float)
    try:
        result_invalid = checker.are_different([1, 2], [3, 4])
    except ValueError as e:
        print(e)