class Calculator:
    def __init__(self):
        self.valid_types = (int, float)

    def _validate_operands(self, a, b):
        if not isinstance(a, self.valid_types) or not isinstance(b, self.valid_types):
            raise ValueError("Both operands must be numbers.")

    def add(self, a, b):
        self._validate_operands(a, b)
        return a + b

if __name__ == '__main__':
    calc = Calculator()
    try:
        result1 = calc.add(8, 4)
        print(f"Result of add(8, 4): {result1}")
        result2 = calc.add(12.5, 7.5)
        print(f"Result of add(12.5, 7.5): {result2}")
    except ValueError as e:
        print(e)