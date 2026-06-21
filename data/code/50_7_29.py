class AreaCalculator:
    def get_difference(self, area_a, area_b):
        self._validate_area(area_a)
        self._validate_area(area_b)
        return abs(area_a - area_b)

    def _validate_area(self, area):
        if not isinstance(area, (int, float)):
            raise ValueError("Area must be a number")

if __name__ == '__main__':
    calculator = AreaCalculator()
    area1 = 20.5
    area2 = 35.75
    difference1 = calculator.get_difference(area1, area2)
    print(f"Difference between {area1} and {area2}: {difference1}")

    area3 = 40.0
    area4 = 20.0
    difference2 = calculator.get_difference(area3, area4)
    print(f"Difference between {area3} and {area4}: {difference2}")