class AreaCalculator:
    def __init__(self, area1, area2):
        if not (isinstance(area1, (int, float)) and isinstance(area2, (int, float))):
            raise ValueError("Both areas must be numbers.")
        self.area1 = area1
        self.area2 = area2

    def calculate_difference(self):
        return abs(self.area1 - self.area2)

if __name__ == '__main__':
    calculator = AreaCalculator(60, 25)
    print(calculator.calculate_difference())