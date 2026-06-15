class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
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
    num5 = 100
    num6 = 30
    print(f"Addition: {calc.add(num5, num6)}")
    print(f"Subtraction: {calc.subtract(num5, num6)}")
    print(f"Multiplication: {calc.multiply(num5, num6)}")
    print(f"Division: {calc.divide(num5, num6)}")
    try:
        calc.divide(10, 0)
    except ZeroDivisionError as e:
        print(f"Error caught: {e}")