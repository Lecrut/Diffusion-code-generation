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
    num3 = 0
    num4 = 10
    print(f"Addition: {calc.add(num1, num2)}")
    print(f"Subtraction: {calc.subtract(num1, num2)}")
    print(f"Multiplication: {calc.multiply(num1, num2)}")
    print(f"Division (20/5): {calc.divide(num1, num2)}")
    try:
        result = calc.divide(num4, num3)
        print(f"Division (10/0): {result}")
    except ZeroDivisionError as e:
        print(f"Error during division: {e}")