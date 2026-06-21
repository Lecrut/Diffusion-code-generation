class ValueChecker:

    def __init__(self):
        self.supported_types = {int, float, str}

    def _validate_type(self, value):
        if type(value) not in self.supported_types:
            raise ValueError(f'Unsupported type: {type(value).__name__}')

    def are_different(self, val1, val2):
        self._validate_type(val1)
        self._validate_type(val2)
        return val1 != val2
if __name__ == '__main__':
    checker = ValueChecker()
    try:
        result_int = checker.are_different(10, 20)
        print('Integers different:', result_int)
        result_str = checker.are_different('hello', 'world')
        print('Strings different:', result_str)
        result_float = checker.are_different(3.14, 2.718)
        print('Floats different:', result_float)
        result_invalid = checker.are_different([1, 2], [1, 2])
    except ValueError as e:
        print(e)