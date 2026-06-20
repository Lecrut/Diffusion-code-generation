class ArithmeticOperations:
    PI = 3.141592653589793
    E = 2.718281828459045

    def add(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError('Both arguments must be integers or floats')
        return a + b

    def subtract(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError('Both arguments must be integers or floats')
        return a - b

    def multiply(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError('Both arguments must be integers or floats')
        return a * b

    def divide(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError('Both arguments must be integers or floats')
        if b == 0:
            raise ValueError('Cannot divide by zero')
        return a / b
if __name__ == '__main__':
    calc = ArithmeticOperations()
    print(calc.add(10, 5))
    print(calc.subtract(10, 5))
    print(calc.multiply(10, 5))
    print(calc.divide(10, 5))