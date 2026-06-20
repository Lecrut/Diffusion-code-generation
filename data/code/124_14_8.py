class ArithmeticOperations:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            raise ValueError("Cannot divide by zero")
        return self.num1 / self.num2

if __name__ == '__main__':
    calculator = ArithmeticOperations(10.5, 3.2)
    print(f"Addition: {calculator.add()}")
    print(f"Subtraction: {calculator.subtract()}")
    print(f"Multiplication: {calculator.multiply()}")
    try:
        print(f"Division: {calculator.divide()}")
    except ValueError as e:
        print(e)