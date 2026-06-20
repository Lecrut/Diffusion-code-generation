class ArithmeticOperations:
    def __init__(self):
        self.constant_int = 10
        self.constant_float = 3.14

    def add(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be integers or floats")
        return a + b

    def subtract(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be integers or floats")
        return a - b

    def multiply(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be integers or floats")
        return a * b

    def divide(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be integers or floats")
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

if __name__ == '__main__':
    calc = ArithmeticOperations()
    print(calc.add(calc.constant_int, calc.constant_float))
    print(calc.subtract(calc.constant_int, calc.constant_float))
    print(calc.multiply(calc.constant_int, calc.constant_float))
    print(calc.divide(calc.constant_int, calc.constant_float))