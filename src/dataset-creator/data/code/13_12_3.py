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
    result_product = operations.multiply(num1, num2)
    result_quotient = operations.divide(num1, num2)
    print(f"Product of {num1} and {num2}: {result_product}")
    print(f"Quotient of {num1} divided by {num2}: {result_quotient}")
    try:
        operations.divide(10, 0)
    except ZeroDivisionError as e:
        print(f"Error caught: {e}")