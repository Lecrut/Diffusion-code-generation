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
    result_int1 = checker.are_different(10, 20)
    print('Integers different (10, 20):', result_int1)
    result_int2 = checker.are_different(30, 30)
    print('Integers different (30, 30):', result_int2)
    result_str1 = checker.are_different('hello', 'world')
    print("Strings different ('hello', 'world'):", result_str1)
    result_str2 = checker.are_different('python', 'python')
    print("Strings different ('python', 'python'):", result_str2)
    result_float1 = checker.are_different(3.14, 2.718)
    print('Floats different (3.14, 2.718):', result_float1)
    result_float2 = checker.are_different(1.618, 1.618)
    print('Floats different (1.618, 1.618):', result_float2)