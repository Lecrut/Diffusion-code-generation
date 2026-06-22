class ValueChecker:
    def __init__(self):
        self.supported_types = (int, float, str)
    
    def _validate_type(self, value):
        if not isinstance(value, self.supported_types):
            raise ValueError(f'Unsupported type: {type(value).__name__}')
    
    def are_different(self, val1, val2):
        self._validate_type(val1)
        self._validate_type(val2)
        return val1 != val2

if __name__ == '__main__':
    checker = ValueChecker()
    result_int = checker.are_different(5, 10)
    result_str = checker.are_different('python', 'java')
    result_float = checker.are_different(3.14, 2.718)
    
    print("Integers different:", result_int)
    print("Strings different:", result_str)
    print("Floats different:", result_float)