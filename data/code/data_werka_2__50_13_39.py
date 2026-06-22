class Rectangle:

    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError('Length and width must be positive numbers.')
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

def calculate_difference(rect1, rect2):
    return abs(rect1.area() - rect2.area())
if __name__ == '__main__':
    try:
        rect1 = Rectangle(9, 3)
        rect2 = Rectangle(6, 7)
        difference = calculate_difference(rect1, rect2)
        print(difference)
    except ValueError as e:
        print(e)