class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

def validate_dimensions(length, width):
    if length <= 0 or width <= 0:
        raise ValueError('Length and width must be positive numbers.')

def find_difference(rect1, rect2):
    return abs(rect1.area() - rect2.area())
if __name__ == '__main__':
    try:
        length1 = 9
        width1 = 3
        length2 = 6
        width2 = 4
        validate_dimensions(length1, width1)
        validate_dimensions(length2, width2)
        rect1 = Rectangle(length1, width1)
        rect2 = Rectangle(length2, width2)
        difference = find_difference(rect1, rect2)
        print(difference)
    except ValueError as e:
        print(e)