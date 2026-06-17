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
            raise ValueError("Cannot divide by zero")
        return a / b
if __name__ == '__main__':
    calc = Calculator()
    num1 = 20
    num2 = 5
    print("Addition:", calc.add(num1, num2))
    print("Subtraction:", calc.subtract(num1, num2))
    print("Multiplication:", calc.multiply(num1, num2))
    print("Division:", calc.divide(num1, num2))
    num3 = 10
    num4 = 3
    print("Addition:", calc.add(num3, num4))
    print("Subtraction:", calc.subtract(num3, num4))
    print("Multiplication:", calc.multiply(num3, num4))
    print("Division:", calc.divide(num3, num4))
    try:
        calc.divide(10, 0)
    except ValueError as e:
        print("Error:", e)