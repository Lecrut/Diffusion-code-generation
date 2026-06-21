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
    result_integers = checker.are_different(42, 24)
    result_strings = checker.are_different('hello', 'world')
    result_floats = checker.are_different(3.14, 3.14)
    print("Integers different:", result_integers)
    print("Strings different:", result_strings)
    print("Floats different:", result_floats)