class ValueChecker:
    def __init__(self):
        self.valid_types = (int, float, str)

    def _validate_input(self, value):
        if not isinstance(value, self.valid_types):
            raise ValueError(f"Unsupported type: {type(value).__name__}. Only integers, floats, and strings are allowed.")

    def are_different(self, val1, val2):
        try:
            self._validate_input(val1)
            self._validate_input(val2)
            return val1 != val2
        except ValueError as e:
            print(f"Error: {e}")
            return False

if __name__ == '__main__':
    checker = ValueChecker()
    result_int = checker.are_different(10, 20)
    result_str = checker.are_different('hello', 'world')
    result_float = checker.are_different(3.14, 3.14)
    result_invalid = checker.are_different([1, 2], [1, 2])
    
    print("Integers different:", result_int)
    print("Strings different:", result_str)
    print("Floats different:", result_float)
    print("Invalid types different:", result_invalid)