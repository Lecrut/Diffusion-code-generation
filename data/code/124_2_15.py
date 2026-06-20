import math

class ArithmeticOperations:
    def __init__(self):
        self.constants = {
            'PI': math.pi,
            'E': math.e
        }

    @staticmethod
    def add(num1, num2):
        return num1 + num2

    @staticmethod
    def subtract(num1, num2):
        return num1 - num2

    @staticmethod
    def multiply(num1, num2):
        return num1 * num2

    @staticmethod
    def divide(num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Division by zero error")

if __name__ == '__main__':
    calc = ArithmeticOperations()
    a = 25.5
    b = 4.2

    print(f"Addition: {calc.add(a, b)}")
    print(f"Subtraction: {calc.subtract(a, b)}")
    print(f"Multiplication: {calc.multiply(a, b)}")
    try:
        print(f"Division: {calc.divide(a, b)}")
    except ValueError as e:
        print(e)