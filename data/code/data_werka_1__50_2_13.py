class AreaDifferenceCalculator:
    def __init__(self):
        self.area1 = 0
        self.area2 = 0

    def set_areas(self, area1, area2):
        if not isinstance(area1, (int, float)) or not isinstance(area2, (int, float)):
            raise ValueError("Both area1 and area2 must be numbers.")
        self.area1 = area1
        self.area2 = area2

    def calculate_difference(self):
        return abs(self.area1 - self.area2)

if __name__ == '__main__':
    calculator = AreaDifferenceCalculator()
    try:
        calculator.set_areas(75.3, 45.8)
        difference = calculator.calculate_difference()
        print(difference)
    except ValueError as e:
        print(e)