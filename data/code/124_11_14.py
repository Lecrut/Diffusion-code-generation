class ArithmeticOperations:

    def __init__(self):
        self.constant_int = 5
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
    arith = ArithmeticOperations()
    print(arith.add(10, 5))
    print(arith.subtract(10, 5))
    print(arith.multiply(10, 5))
    print(arith.divide(10, 5))