class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

if __name__ == '__main__':
    calc = Calculator(10.5, 3.2)
    print(f"Addition: {Calculator.add(calc.num1, calc.num2)}")
    print(f"Subtraction: {Calculator.subtract(calc.num1, calc.num2)}")
    print(f"Multiplication: {Calculator.multiply(calc.num1, calc.num2)}")
    try:
        print(f"Division: {Calculator.divide(calc.num1, calc.num2)}")
    except ValueError as e:
        print(e)