def find_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return area ** 0.5

class SquareCalculator:
    def __init__(self, area):
        self.area = area

    def calculate_side_length(self):
        return find_side_length(self.area)

if __name__ == '__main__':
    sample_areas = [16, 25, 49]
    for area in sample_areas:
        calculator = SquareCalculator(area)
        side_length = calculator.calculate_side_length()
        print(f"The side length of a square with area {area} is {side_length}")