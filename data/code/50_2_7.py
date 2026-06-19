def validate_area(area):
    if not isinstance(area, (int, float)):
        raise ValueError("Area must be a number")

class AreaDifferenceCalculator:
    def calculate_difference(self, area1, area2):
        validate_area(area1)
        validate_area(area2)
        return abs(area1 - area2)

if __name__ == '__main__':
    calculator = AreaDifferenceCalculator()
    area_a = 75.5
    area_b = 30.5
    difference = calculator.calculate_difference(area_a, area_b)
    print(difference)