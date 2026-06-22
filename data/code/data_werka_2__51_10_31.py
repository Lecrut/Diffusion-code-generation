class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

def validate_dimensions(width, height):
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise ValueError("Width and height must be numbers.")
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive numbers.")

if __name__ == '__main__':
    try:
        width = 6.0
        height = 4.0
        validate_dimensions(width, height)
        rect = Rectangle(width, height)
        print(rect.perimeter())
    except ValueError as e:
        print(f"Error: {e}")