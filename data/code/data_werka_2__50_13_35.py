class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

def calculate_area_difference(rect1, rect2):
    try:
        return abs(rect1.area() - rect2.area())
    except AttributeError as e:
        raise ValueError("Both inputs must be instances of Rectangle.") from e

if __name__ == '__main__':
    try:
        rect1 = Rectangle(9, 3)
        rect2 = Rectangle(6, 7)
        difference = calculate_area_difference(rect1, rect2)
        print(difference)
    except ValueError as e:
        print(e)