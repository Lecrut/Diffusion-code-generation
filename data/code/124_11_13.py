class ArithmeticOperations:
    def __init__(self):
        self.constant_int = 10
        self.constant_float = 3.14

    def add(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b
        else:
            raise TypeError("Both operands must be integers or floats")

    def subtract(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a - b
        else:
            raise TypeError("Both operands must be integers or floats")

    def multiply(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a * b
        else:
            raise TypeError("Both operands must be integers or floats")

    def divide(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)) and b != 0:
            return a / b
        elif b == 0:
            raise ValueError("Cannot divide by zero")
        else:
            raise TypeError("Both operands must be integers or floats")

if __name__ == '__main__':
    arithmetic = ArithmeticOperations()
    print(arithmetic.add(5, 3))
    print(arithmetic.subtract(10, 4.5))
    print(arithmetic.multiply(7, 2))
    try:
        print(arithmetic.divide(8, 0))
    except ValueError as e:
        print(e)