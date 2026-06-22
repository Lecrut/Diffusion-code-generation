class AreaCalculator:
    MAX_AREA = 10000.0
    MIN_AREA = 0.0

    @staticmethod
    def validate_area(area):
        if not (AreaCalculator.MIN_AREA <= area <= AreaCalculator.MAX_AREA):
            raise ValueError(f"Area must be between {AreaCalculator.MIN_AREA} and {AreaCalculator.MAX_AREA}")

    def get_difference(self, area_a, area_b):
        AreaCalculator.validate_area(area_a)
        AreaCalculator.validate_area(area_b)
        return abs(area_a - area_b)

if __name__ == '__main__':
    calculator = AreaCalculator()
    try:
        area1 = 75.2
        area2 = 48.9
        difference = calculator.get_difference(area1, area2)
        print(f"The positive difference is: {difference:.2f}")
    except ValueError as e:
        print(e)