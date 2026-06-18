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
    try:
        operations.divide(10, 0)
    except ValueError as e:
        print(f"Error caught: {e}")