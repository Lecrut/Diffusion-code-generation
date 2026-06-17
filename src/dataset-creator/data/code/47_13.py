class Calculator:
    def multiply(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("Both operands must be integers.")
        return a * b
if __name__ == '__main__':
    calc = Calculator()
    result_1 = calc.multiply(42, -8)
    print(f"Result of {result_1}")
    result_2 = calc.multiply(0, 999)
    print(f"Result of {result_2}")
    try:
        invalid_result = calc.multiply("5", 3)
    except TypeError as e:
        print(f"Error caught for non-integer input: {e}")
    result_3 = calc.multiply(10**9, -2 * 10**8)
    print(f"Result of large integer multiplication: {result_3}")