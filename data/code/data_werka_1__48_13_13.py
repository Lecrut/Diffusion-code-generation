import math

class EquilateralTriangle:
    def __init__(self, height):
        self.height = height
        self.side_length = 2 * height / math.sqrt(3)
        self.perimeter = 3 * self.side_length

    def get_side_length(self):
        return self.side_length

    def get_perimeter(self):
        return self.perimeter

if __name__ == '__main__':
    triangle_height = 8.73
    triangle = EquilateralTriangle(triangle_height)
    print(f'Side Length: {triangle.get_side_length()}')
    print(f'Perimeter: {triangle.get_perimeter()}')