class ValueChecker:

    def __init__(self):
        self.supported_types = (int, float, str)

    def _is_supported_type(self, value):
        return isinstance(value, self.supported_types)

    def are_different(self, val1, val2):
        if not self._is_supported_type(val1) or not self._is_supported_type(val2):
            raise ValueError(f'Unsupported type: {type(val1).__name__} or {type(val2).__name__}')
        return val1 != val2
if __name__ == '__main__':
    checker = ValueChecker()
    int_result = checker.are_different(100, 200)
    print('Integers different:', int_result)
    str_result = checker.are_different('apple', 'banana')
    print('Strings different:', str_result)
    float_result = checker.are_different(3.14159, 2.71828)
    print('Floats different:', float_result)
    try:
        unsupported_result = checker.are_different([1, 2], [3, 4])
        print('Unsupported types result:', unsupported_result)
    except ValueError as e:
        print(e)