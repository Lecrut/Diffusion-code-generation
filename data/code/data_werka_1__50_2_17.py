class AreaDifferenceCalculator:
    def __init__(self, area1, area2):
        if not all(isinstance(area, (int, float)) for area in [area1, area2]):
            raise ValueError("Both area1 and area2 must be numbers.")
        self.area1 = area1
        self.area2 = area2

    def calculate_difference(self):
        return abs(self.area1 - self.area2)

if __name__ == '__main__':
    try:
        calculator = AreaDifferenceCalculator(100, 45)
        difference = calculator.calculate_difference()
        print(difference)
    except ValueError as e:
        print(e)