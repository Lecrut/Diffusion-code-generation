class Calculator:
    def multiply(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("Both operands must be integers.")
        return a * b
if __name__ == '__main__':
    calc = Calculator()
    try:
        result1 = calc.multiply(4, 5)
        print(f"Result of {4} x {5}: {result1}")
        result2 = calc.multiply("3", "6")
        print(f"Unexpected success: {result2}")
    except TypeError as e:
        print(f"Error occurred: {e}")
    try:
        result3 = calc.multiply(10, 7)
        print(f"Result of {10} x {7}: {result3}")
    except Exception as e:
        print(f"Unexpected error: {e}")