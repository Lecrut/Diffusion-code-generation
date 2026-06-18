class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
if __name__ == '__main__':
    calc = Calculator()
    num1 = 20
    num2 = 5
    num3 = 10
    num4 = 2
    print(f"Addition: {calc.add(num1, num2)}")
    print(f"Subtraction: {calc.subtract(num1, num2)}")
    print(f"Multiplication: {calc.multiply(num1, num2)}")
    print(f"Division: {calc.divide(num1, num2)}")
    try:
        result = calc.divide(10, 0)
    except ValueError as e:
        print(f"Error: {e}")