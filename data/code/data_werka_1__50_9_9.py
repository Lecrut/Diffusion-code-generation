class AreaCalculator:
    TOLERANCE = 1e-9

    @staticmethod
    def is_valid_area(area):
        return isinstance(area, (int, float)) and area >= 0

    def get_difference(self, area_a, area_b):
        if not (self.is_valid_area(area_a) and self.is_valid_area(area_b)):
            raise ValueError("Both areas must be non-negative numbers.")
        difference = abs(area_a - area_b)
        return round(difference, 9)

if __name__ == '__main__':
    calculator = AreaCalculator()
    try:
        area1 = 75.234
        area2 = 30.123
        difference = calculator.get_difference(area1, area2)
        print(f"The positive difference is: {difference:.9f}")
    except ValueError as e:
        print(e)