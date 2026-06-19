class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

def validate_dimensions(width, height):
    if not isinstance(width, int) or not isinstance(height, int):
        raise ValueError("Width and height must be integers.")
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive integers.")

if __name__ == '__main__':
    try:
        validate_dimensions(9, 2)
        rect = Rectangle(9, 2)
        print(rect.perimeter())
    except ValueError as e:
        print(e)