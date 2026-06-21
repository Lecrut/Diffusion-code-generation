class Calculator:
    def __init__(self):
        self.supported_operations = ['add']

    def validate_numbers(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both operands must be numbers.")

    def add(self, a, b):
        self.validate_numbers(a, b)
        return a + b

if __name__ == '__main__':
    calc = Calculator()
    try:
        result1 = calc.add(8, 12)
        print(f"Result of add(8, 12): {result1}")
        result2 = calc.add(3.5, 4.7)
        print(f"Result of add(3.5, 4.7): {result2}")
    except ValueError as e:
        print(e)