import math

class SquareCalculator:
    def __init__(self, area):
        if area < 0:
            raise ValueError("Area cannot be negative")
        self.area = area

    def calculate_side_length(self):
        return math.sqrt(self.area)

if __name__ == '__main__':
    sample_areas = [
        {'description': 'small', 'area': 9.0},
        {'description': 'medium', 'area': 16.0},
        {'description': 'large', 'area': 25.0}
    ]

    for item in sample_areas:
        try:
            calculator = SquareCalculator(item['area'])
            side_length = calculator.calculate_side_length()
            print(f"The side length of the {item['description']} square is: {side_length}")
        except ValueError as e:
            print(e)