class Calculator:
    def add(self, x, y):
        return x + y
    def subtract(self, x, y):
        return x - y
    def multiply(self, x, y):
        return x * y
    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y
if __name__ == '__main__':
    calc = Calculator()
    print(f"Addition: {calc.add(10, 5)}")
    print(f"Subtraction: {calc.subtract(10, 5)}")
    print(f"Multiplication: {calc.multiply(10, 5)}")
    print(f"Division: {calc.divide(10, 5)}")
    try:
        print(f"Division by zero test: {calc.divide(10, 0)}")
    except ValueError as e:
        print(f"Error caught: {e}")