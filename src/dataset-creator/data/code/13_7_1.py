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
    result_mult = operations.multiply(num1, num2)
    result_div = operations.divide(num1, num2)
    print(f"Multiplication of {num1} and {num2}: {result_mult}")
    print(f"Division of {num1} by {num2}: {result_div}")
    num3 = 15
    num4 = 3
    result_mult2 = operations.multiply(num3, num4)
    result_div2 = operations.divide(num3, num4)
    print(f"Multiplication of {num3} and {num4}: {result_mult2}")
    print(f"Division of {num3} by {num4}: {result_div2}")