class ArithmeticOperations:
    def __init__(self):
        self.constant_int = 10
        self.constant_float = 3.14

    def add(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b
        else:
            raise TypeError("Both inputs must be integers or floats")

    def subtract(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a - b
        else:
            raise TypeError("Both inputs must be integers or floats")

    def multiply(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a * b
        else:
            raise TypeError("Both inputs must be integers or floats")

    def divide(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)) and b != 0:
            return a / b
        elif b == 0:
            raise ValueError("Cannot divide by zero")
        else:
            raise TypeError("Both inputs must be integers or floats")

if __name__ == '__main__':
    calc = ArithmeticOperations()
    print(calc.add(calc.constant_int, calc.constant_float))
    print(calc.subtract(calc.constant_int, calc.constant_float))
    print(calc.multiply(calc.constant_int, calc.constant_float))
    print(calc.divide(calc.constant_int, calc.constant_float))