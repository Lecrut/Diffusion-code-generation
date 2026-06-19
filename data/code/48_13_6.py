import math

class EquilateralTriangle:
    def __init__(self, height):
        self.height = height
        self.side_length = self._calculate_side_length()
        self.perimeter = self._calculate_perimeter()

    @staticmethod
    def _calculate_side_length(height):
        return 2 * height / math.sqrt(3)

    @staticmethod
    def _calculate_perimeter(side_length):
        return 3 * side_length

if __name__ == '__main__':
    triangle_height = 8.73
    triangle = EquilateralTriangle(triangle_height)
    print(f'Side Length: {triangle.side_length}')
    print(f'Perimeter: {triangle.perimeter}')