class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        if not (isinstance(length, (int, float)) and isinstance(width, (int, float))):
            raise TypeError("Length and width must be numbers.")
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")

    def get_perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    try:
        rect = Rectangle(9, 3)
        print(rect.get_perimeter())
    except (TypeError, ValueError) as e:
        print(e)