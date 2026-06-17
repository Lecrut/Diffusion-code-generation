class Calculator:
    def multiply(self, a, b):
        try:
            int(a)
            int(b)
        except ValueError:
            raise TypeError("Both operands must be integers.")
        return int(a) * int(b)
if __name__ == '__main__':
    calc = Calculator()
    result1 = calc.multiply(5, 3)
    print(f"Result of {5} and {3}: {result1}")
    try:
        result2 = calc.multiply("4", "7")
    except TypeError as e:
        print(f"Error occurred with string inputs: {e}")