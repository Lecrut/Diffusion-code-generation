class AreaCalculator:
    def __init__(self, area1_str, area2_str):
        self.area1_str = area1_str
        self.area2_str = area2_str

    def convert_to_float(self, area_str):
        try:
            return float(area_str)
        except ValueError as e:
            print(f"ValueError: {e}")
            return None

    def calculate_difference(self):
        area1 = self.convert_to_float(self.area1_str)
        area2 = self.convert_to_float(self.area2_str)
        if area1 is not None and area2 is not None:
            return abs(area1 - area2)
        return None

if __name__ == '__main__':
    sample_area1 = "75.2"
    sample_area2 = "23.8"
    calculator = AreaCalculator(sample_area1, sample_area2)
    difference = calculator.calculate_difference()
    if difference is not None:
        print(difference)

    another_sample_area1 = "150.0"
    another_sample_area2 = "100.0"
    another_calculator = AreaCalculator(another_sample_area1, another_sample_area2)
    another_difference = another_calculator.calculate_difference()
    if another_difference is not None:
        print(another_difference)