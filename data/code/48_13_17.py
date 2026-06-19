import math

class EquilateralTriangle:
    def __init__(self, height):
        self.height = height

    def calculate_side_length(self):
        return 2 * self.height / math.sqrt(3)

    def calculate_perimeter(self):
        side_length = self.calculate_side_length()
        return 3 * side_length

if __name__ == '__main__':
    triangle = EquilateralTriangle(height=8.73)
    side_length = triangle.calculate_side_length()
    perimeter = triangle.calculate_perimeter()
    print(f'Side Length: {side_length}')
    print(f'Perimeter: {perimeter}')