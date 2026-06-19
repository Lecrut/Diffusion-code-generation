class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

def calculate_area(width, height):
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive numbers.")
    rectangle = Rectangle(width, height)
    return rectangle.area()

if __name__ == '__main__':
    sample_width = 5
    sample_height = 10
    try:
        result = calculate_area(sample_width, sample_height)
        print(result)
    except ValueError as e:
        print(e)