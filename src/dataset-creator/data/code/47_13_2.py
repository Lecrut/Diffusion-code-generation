class Calculator:
    def multiply(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("Both operands must be integers.")
        return a * b
if __name__ == '__main__':
    calc = Calculator()
    result_1 = calc.multiply(42, -7)
    print(f"Result of {result_1}")
    try:
        invalid_result = calc.multiply(5.0, 3)
    except TypeError as e:
        print(f"Caught expected error for floats: {e}")
    result_2 = calc.multiply(10**9, 0)
    print(f"Result of {result_2}")