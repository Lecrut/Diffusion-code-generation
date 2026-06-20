class ArithmeticOperations:

    def __init__(self):
        self.constant_int = 42
        self.constant_float = 3.14

    def add(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b
        else:
            raise TypeError('Both operands must be integers or floats')

    def subtract(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a - b
        else:
            raise TypeError('Both operands must be integers or floats')

    def multiply(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a * b
        else:
            raise TypeError('Both operands must be integers or floats')

    def divide(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)) and (b != 0):
            return a / b
        elif b == 0:
            raise ValueError('Cannot divide by zero')
        else:
            raise TypeError('Both operands must be integers or floats')
if __name__ == '__main__':
    arithmetic = ArithmeticOperations()
    print(arithmetic.add(10, 5))
    print(arithmetic.subtract(10, 5))
    print(arithmetic.multiply(10, 5))
    print(arithmetic.divide(10, 5))