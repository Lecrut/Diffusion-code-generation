class ArithmeticOperations:
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
    num1 = 10
    num2 = 5
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")
    print(f"Sum: {ArithmeticOperations.add(num1, num2)}")
    print(f"Difference: {ArithmeticOperations.subtract(num1, num2)}")
    print(f"Product: {ArithmeticOperations.multiply(num1, num2)}")