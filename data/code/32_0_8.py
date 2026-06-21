AREA_UNIT_CONVERSION = 1.0

def _validate_dimension(value, name):
    if value < 0:
        raise ValueError(f"{name} cannot be negative")

def calculate_rectangle_area(width, height):
    _validate_dimension(width, "Width")
    _validate_dimension(height, "Height")
    return width * height * AREA_UNIT_CONVERSION

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return calculate_rectangle_area(self.width, self.height)

if __name__ == '__main__':
    test_width = 7
    test_height = 3
    rect = Rectangle(test_width, test_height)
    print(rect.get_area())
    print(calculate_rectangle_area(12.5, 4.0))