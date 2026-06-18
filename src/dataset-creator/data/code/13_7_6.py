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
    print(f"Multiplication of {num1} and {num2}: {result_mult}")
    num3 = 20
    num4 = 4
    result_div = operations.divide(num3, num4)
    print(f"Division of {num3} by {num4}: {result_div}")
    try:
        operations.divide(10, 0)
    except ValueError as e:
        print(f"Error caught: {e}")