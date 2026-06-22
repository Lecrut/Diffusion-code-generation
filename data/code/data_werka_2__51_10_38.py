class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

def calculate_rectangle_perimeter(dimensions):
    try:
        rect = Rectangle(dimensions['width'], dimensions['height'])
        return rect.perimeter()
    except KeyError as e:
        raise ValueError(f"Missing dimension: {e}")

if __name__ == '__main__':
    sample_dimensions = {'width': 6.0, 'height': 4.0}
    perimeter = calculate_rectangle_perimeter(sample_dimensions)
    print(perimeter)