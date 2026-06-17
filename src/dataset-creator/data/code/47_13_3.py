class Calculator:
    def multiply(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("Both operands must be integers.")
        return a * b
if __name__ == '__main__':
    calc = Calculator()
    result_valid = calc.multiply(4, 5)
    print(f"Result of {result_valid}")
    try:
        calc.multiply(3.0, 7)
    except TypeError as e:
        print(f"Error caught for float input: {e}")
    result_negative = calc.multiply(-10, -2)
    print(f"Result of negative multiplication: {result_negative}")
    try:
        calc.multiply("5", "6")
    except TypeError as e:
        print(f"Error caught for string input: {e}")