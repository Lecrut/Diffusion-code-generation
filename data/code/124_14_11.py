def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def perform_operation(self, operation):
        operations = {
            '+': add,
            '-': subtract,
            '*': multiply,
            '/': divide
        }
        return operations.get(operation, lambda x, y: 'Invalid operation')(self.num1, self.num2)

if __name__ == '__main__':
    calc = Calculator(7.5, 3.0)
    print(f"Addition: {calc.perform_operation('+')}")
    print(f"Subtraction: {calc.perform_operation('-')}")
    print(f"Multiplication: {calc.perform_operation('*')}")