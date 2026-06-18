class Calculator:
    def multiply(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("Both operands must be integers.")
        return a * b
if __name__ == '__main__':
    calc = Calculator()
    result1 = calc.multiply(4, 5)
    print(f"Result: {result1}")
    try:
        result2 = calc.multiply("3", 6)
    except TypeError as e:
        print(f"Error: {e}")
    try:
        result3 = calc.multiply(2.0, 4)
    except TypeError as e:
        print(f"Error: {e}")