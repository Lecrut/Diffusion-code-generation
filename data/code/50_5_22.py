class DifferenceCalculator:
    def __init__(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Inputs must be numbers")
        self.a = a
        self.b = b

    def compute_difference(self):
        return abs(self.a - self.b)

if __name__ == '__main__':
    calculator = DifferenceCalculator(20, 10)
    print(calculator.compute_difference())