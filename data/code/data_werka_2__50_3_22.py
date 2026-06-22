class AreaCalculator:
    def __init__(self, area1_str, area2_str):
        self.area1 = self._parse_area(area1_str)
        self.area2 = self._parse_area(area2_str)

    def _parse_area(self, area_str):
        try:
            return float(area_str)
        except ValueError as e:
            print(f"Error: {e}")
            return None

    def calculate_difference(self):
        if self.area1 is not None and self.area2 is not None:
            return abs(self.area1 - self.area2)
        return None

if __name__ == '__main__':
    area_calculator = AreaCalculator("45.67", "30.12")
    difference = area_calculator.calculate_difference()
    if difference is not None:
        print(difference)