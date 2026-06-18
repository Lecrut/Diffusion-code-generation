class Calculator:
    def multiply(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("Both operands must be integers.")
        return a * b
if __name__ == '__main__':
    calc = Calculator()
    try:
        result1 = calc.multiply(4, 5)
        print(f"Result of multiplying {4} and {5}: {result1}")
        result2 = calc.multiply("6", 7)
        print(result2)
    except TypeError as e:
        print(f"Error occurred: {e}")