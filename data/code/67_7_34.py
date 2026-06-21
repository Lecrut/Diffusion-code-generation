class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both operands must be numbers.")
        self.result = a + b
        return self.result

if __name__ == '__main__':
    calc = Calculator()
    try:
        result1 = calc.add(8, 4)
        print(f"Result of add(8, 4): {result1}")
        result2 = calc.add(-3.5, 7.2)
        print(f"Result of add(-3.5, 7.2): {result2}")
    except ValueError as e:
        print(e)