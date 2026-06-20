DIMENSION_MAP = {
    "length": "horizontal_axis",
    "width": "vertical_axis"
}

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    side_lengths = DIMENSION_MAP
    rect = Rectangle(8, 3)
    perimeter = rect.get_perimeter()
    print(perimeter)