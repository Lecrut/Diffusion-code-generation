class MathOperations:
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
if __name__ == '__main__':
    operations = MathOperations()
    num1 = 10
    num2 = 5
    product = operations.multiply(num1, num2)
    quotient = operations.divide(num1, num2)
    print(f"The product of {num1} and {num2} is: {product}")
    print(f"The quotient of {num1} divided by {num2} is: {quotient}")
    num3 = 15
    num4 = 3
    product2 = operations.multiply(num3, num4)
    quotient2 = operations.divide(num3, num4)
    print(f"The product of {num3} and {num4} is: {product2}")
    print(f"The quotient of {num3} divided by {num4} is: {quotient2}")