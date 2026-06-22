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
    result_int = checker.are_different(42, 7)
    result_str = checker.are_different('hello', 'world')
    result_float = checker.are_different(3.14, 2.718)
    result_same_int = checker.are_different(5, 5)
    result_same_str = checker.are_different('python', 'python')
    result_same_float = checker.are_different(2.718, 2.718)

    print("Integers different:", result_int)
    print("Strings different:", result_str)
    print("Floats different:", result_float)
    print("Same integers different:", result_same_int)
    print("Same strings different:", result_same_str)
    print("Same floats different:", result_same_float)