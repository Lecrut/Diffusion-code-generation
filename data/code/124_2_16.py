import math
DIVISION_THRESHOLD = 1e-09

class ArithmeticOperations:

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if abs(num2) < DIVISION_THRESHOLD:
            return 'Error: Division by zero'
        else:
            return num1 / num2
if __name__ == '__main__':
    calculator = ArithmeticOperations()
    a = 25.5
    b = 4.2
    print(calculator.add(a, b))
    print(calculator.subtract(a, b))
    print(calculator.multiply(a, b))
    print(calculator.divide(a, b))