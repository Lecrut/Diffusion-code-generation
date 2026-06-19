class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

def validate_dimensions(length, width):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError('Length and width must be numbers.')
    if length <= 0 or width <= 0:
        raise ValueError('Length and width must be positive.')
if __name__ == '__main__':
    try:
        rect1 = Rectangle(6, 4)
        perimeter1 = rect1.calculate_perimeter()
        print(perimeter1)
        rect2 = Rectangle(8, 2)
        perimeter2 = rect2.calculate_perimeter()
        print(perimeter2)
        rect3 = Rectangle(-5, 3)
    except (TypeError, ValueError) as e:
        print(e)