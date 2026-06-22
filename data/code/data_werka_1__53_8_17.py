def find_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return area ** 0.5

class SquareCalculator:
    def __init__(self, area):
        self.area = area

    def calculate_side_length(self):
        try:
            return find_side_length(self.area)
        except ValueError as e:
            return str(e)

if __name__ == '__main__':
    sample_areas = [16, 49, -10]
    for area in sample_areas:
        calculator = SquareCalculator(area)
        side_length = calculator.calculate_side_length()
        print(f"The side length of the square with area {area} is: {side_length}")