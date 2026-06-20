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
    
    def add(self):
        return add(self.num1, self.num2)
    
    def subtract(self):
        return subtract(self.num1, self.num2)
    
    def multiply(self):
        return multiply(self.num1, self.num2)
    
    def divide(self):
        return divide(self.num1, self.num2)

if __name__ == '__main__':
    num1 = 10.5
    num2 = 3.2
    calc = Calculator(num1, num2)
    print(f"Addition: {calc.add()}")
    print(f"Subtraction: {calc.subtract()}")
    print(f"Multiplication: {calc.multiply()}")
    try:
        print(f"Division: {calc.divide()}")
    except ValueError as e:
        print(e)