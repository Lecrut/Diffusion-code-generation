class AreaDifferenceCalculator:
    def __init__(self):
        self.area1 = None
        self.area2 = None

    def set_area(self, area_index, area_str):
        try:
            if area_index == 1:
                self.area1 = float(area_str)
            elif area_index == 2:
                self.area2 = float(area_str)
            else:
                raise ValueError("Invalid area index")
        except ValueError as e:
            print(f"Error: {e}")

    def calculate_difference(self):
        if self.area1 is not None and self.area2 is not None:
            return abs(self.area1 - self.area2)
        return None

if __name__ == '__main__':
    calculator = AreaDifferenceCalculator()
    calculator.set_area(1, "45.67")
    calculator.set_area(2, "30.12")
    difference = calculator.calculate_difference()
    if difference is not None:
        print(difference)