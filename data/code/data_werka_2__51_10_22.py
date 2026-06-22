class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers.")
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

def calculate_perimeter(width, height):
    try:
        rect = Rectangle(width, height)
        return rect.perimeter()
    except ValueError as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    width = 7.5
    height = 2.0
    perimeter = calculate_perimeter(width, height)
    if perimeter is not None:
        print(perimeter)