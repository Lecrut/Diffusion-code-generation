class ArithmeticOperations:
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
    calculator = ArithmeticOperations()
    num1 = 10
    num2 = 5
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")
    print(f"Sum: {calculator.add(num1, num2)}")
    print(f"Difference: {calculator.subtract(num1, num2)}")
    print(f"Product: {calculator.multiply(num1, num2)}")
    print(f"Quotient: {calculator.divide(num1, num2)}")