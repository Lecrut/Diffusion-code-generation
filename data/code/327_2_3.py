class Calculator:
    def __init__(self):
        pass
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
    print(f"Addition: {calc.add(num1, num2)}")
    print(f"Subtraction: {calc.subtract(num1, num2)}")
    print(f"Multiplication: {calc.multiply(num1, num2)}")
    print(f"Division: {calc.divide(num1, num2)}")
    num3 = 10
    num4 = 3
    print(f"\nAddition: {calc.add(num3, num4)}")
    print(f"Subtraction: {calc.subtract(num3, num4)}")
    print(f"Multiplication: {calc.multiply(num3, num4)}")
    print(f"Division: {calc.divide(num3, num4)}")
    try:
        calc.divide(10, 0)
    except ZeroDivisionError as e:
        print(f"\nError caught: {e}")