class AreaDifferenceCalculator:
    def __init__(self, area1, area2):
        if not (isinstance(area1, (int, float)) and isinstance(area2, (int, float))):
            raise ValueError("Both area1 and area2 must be numbers.")
        self.area1 = area1
        self.area2 = area2

    def calculate_difference(self):
        return self.area1 - self.area2

if __name__ == '__main__':
    try:
        calculator = AreaDifferenceCalculator(100, 50)
        difference = calculator.calculate_difference()
        print(difference)
    except ValueError as e:
        print(e)