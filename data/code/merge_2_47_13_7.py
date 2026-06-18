class Calculator:
    def multiply(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("Both operands must be integers.")
        return a * b
if __name__ == '__main__':
    calc = Calculator()
    result_1 = calc.multiply(42, -3)
    print(f"Result of {result_1}")
    try:
        result_float = calc.multiply(5.0, 6)
    except TypeError as e:
        print(f"Error caught for float input: {e}")
    result_2 = calc.multiply(1, 0)
    print(f"Result of {result_2}")