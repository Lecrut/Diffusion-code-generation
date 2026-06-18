class Calculator:
    def multiply(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("Both operands must be integers.")
        return a * b
if __name__ == '__main__':
    calc = Calculator()
    result1 = calc.multiply(4, -3)
    print(f"Result of {4} * {-3}: {result1}")
    result2 = calc.multiply(0, 5)
    print(f"Result of {0} * {5}: {result2}")
    try:
        invalid_result = calc.multiply(3.5, 4)
    except TypeError as e:
        print(f"Error caught for float input: {e}")
    try:
        invalid_result = calc.multiply("2", "3")
    except TypeError as e:
        print(f"Error caught for string input: {e}")