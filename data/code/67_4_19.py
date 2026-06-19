class SumCalculator:
    def __init__(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both a and b must be numbers.")
        self.a = a
        self.b = b

    def calculate(self):
        return self.a + self.b

if __name__ == '__main__':
    try:
        calculator = SumCalculator(4, 6)
        print(calculator.calculate())
    except ValueError as e:
        print(e)