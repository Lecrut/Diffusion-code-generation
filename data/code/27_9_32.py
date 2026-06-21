class ValueChecker:

    def __init__(self):
        self.supported_types = (int, float, str)

    def are_different(self, val1, val2):
        if not isinstance(val1, self.supported_types) or not isinstance(val2, self.supported_types):
            raise ValueError('Unsupported type. Only integers, floats, and strings are supported.')
        return val1 != val2
if __name__ == '__main__':
    checker = ValueChecker()
    try:
        result_int = checker.are_different(42, 7)
        print(result_int)
        result_str = checker.are_different('hello', 'world')
        print(result_str)
        result_float = checker.are_different(3.14, 3.14)
        print(result_float)
        result_invalid = checker.are_different([1, 2], [1, 2])
    except ValueError as e:
        print(e)