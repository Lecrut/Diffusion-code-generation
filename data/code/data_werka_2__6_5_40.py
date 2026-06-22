class WeightCalculator:
    def __init__(self, x, y):
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            raise ValueError("Both inputs must be numbers.")
        self.x = x
        self.y = y

    def calculate_difference(self):
        return abs(self.x - self.y)

if __name__ == '__main__':
    calculator = WeightCalculator(10, 5)
    print(calculator.calculate_difference())