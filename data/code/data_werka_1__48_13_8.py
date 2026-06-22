import math

class EquilateralTriangle:
    def __init__(self, height):
        if height <= 0:
            raise ValueError("Height must be positive")
        self.height = height
        self.side_length = self._calculate_side_length()
        self.perimeter = self._calculate_perimeter()

    def _calculate_side_length(self):
        return (2 * self.height) / math.sqrt(3)

    def _calculate_perimeter(self):
        return 3 * self.side_length

if __name__ == '__main__':
    try:
        height = 8.73
        triangle = EquilateralTriangle(height)
        print(f'Side Length: {triangle.side_length}')
        print(f'Perimeter: {triangle.perimeter}')
    except ValueError as e:
        print(e)