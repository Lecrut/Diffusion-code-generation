class Calculator:
    def multiply(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("Both operands must be integers.")
        return a * b
if __name__ == '__main__':
    calc = Calculator()
    result1 = calc.multiply(4, -3)
    print(f"Result of {4} * {-3}: {result1}")
    try:
        result2 = calc.multiply(5.0, 6)
    except TypeError as e:
        print(f"Error with float input: {e}")
    result3 = calc.multiply(100, 0)
    print(f"Result of {100} * {0}: {result3}")