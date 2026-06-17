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
    result1 = calc.multiply(4, 5)
    print(f"Result: {result1}")