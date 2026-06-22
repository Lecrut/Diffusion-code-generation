class Calculator:
    def __init__(self):
        self.valid_types = (int, float)
    
    def is_valid_operand(self, operand):
        return isinstance(operand, self.valid_types)
    
    def add(self, a, b):
        if not self.is_valid_operand(a) or not self.is_valid_operand(b):
            raise ValueError("Both operands must be numbers.")
        return a + b

if __name__ == '__main__':
    calc = Calculator()
    try:
        result1 = calc.add(8, 4)
        print(f"Result of add(8, 4): {result1}")
        result2 = calc.add(12.7, 5.3)
        print(f"Result of add(12.7, 5.3): {result2}")
    except ValueError as e:
        print(e)