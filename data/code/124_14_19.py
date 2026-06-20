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
    print(f"Addition: {calc.add()}")
    print(f"Subtraction: {calc.subtract()}")
    print(f"Multiplication: {calc.multiply()}")
    try:
        print(f"Division: {calc.divide()}")
    except ValueError as e:
        print(e)