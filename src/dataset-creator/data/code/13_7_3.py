class MathOperations:
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
if __name__ == '__main__':
    operations = MathOperations()
    num1 = 10
    num2 = 5
    num3 = 15
    num4 = 3
    product = operations.multiply(num1, num2)
    quotient = operations.divide(num3, num4)
    print(f"Multiplication of {num1} and {num2}: {product}")
    print(f"Division of {num3} by {num4}: {quotient}")