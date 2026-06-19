class AreaCalculator:
    def __init__(self, area1_str, area2_str):
        self.area1 = self._convert_to_float(area1_str)
        self.area2 = self._convert_to_float(area2_str)

    def _convert_to_float(self, value_str):
        try:
            return float(value_str)
        except ValueError as e:
            print(f"ValueError: {e}")
            return None

    def calculate_difference(self):
        if self.area1 is not None and self.area2 is not None:
            return abs(self.area1 - self.area2)
        return None

if __name__ == '__main__':
    area_calculator = AreaCalculator("100.5", "45.3")
    difference = area_calculator.calculate_difference()
    if difference is not None:
        print(difference)

    another_area_calculator = AreaCalculator("invalid", "45.3")
    another_difference = another_area_calculator.calculate_difference()
    if another_difference is not None:
        print(another_difference)