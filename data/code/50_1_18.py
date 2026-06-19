class AreaCalculator:
    def __init__(self):
        self.MIN_AREA = 0

    def validate_area(self, area):
        if not isinstance(area, (int, float)):
            raise ValueError("Area must be an integer or float.")
        if area < self.MIN_AREA:
            raise ValueError("Area cannot be negative.")

    def calculate_difference(self, area1, area2):
        self.validate_area(area1)
        self.validate_area(area2)
        return abs(area1 - area2)

if __name__ == '__main__':
    calculator = AreaCalculator()
    a = 300
    b = 125.75
    result = calculator.calculate_difference(a, b)
    print(result)