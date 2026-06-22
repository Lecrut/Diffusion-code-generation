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
    dimensions = {'width': 6.0, 'height': 4.0}
    perimeter_value = calculate_perimeter(dimensions['width'], dimensions['height'])
    if perimeter_value is not None:
        print(perimeter_value)