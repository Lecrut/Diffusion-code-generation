import math

class ArithmeticOperations:
    def add(self, num1, num2):
        return num1 + num2
    
    def subtract(self, num1, num2):
        return num1 - num2
    
    def multiply(self, num1, num2):
        return num1 * num2
    
    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Division by zero error"

if __name__ == '__main__':
    calc = ArithmeticOperations()
    a = 25.5
    b = 4.2
    print(calc.add(a, b))
    print(calc.subtract(a, b))
    print(calc.multiply(a, b))
    print(calc.divide(a, b))