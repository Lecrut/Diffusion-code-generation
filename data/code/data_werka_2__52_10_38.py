class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def validate_dimensions(self):
        if self.length <= 0 or self.width <= 0:
            raise ValueError("Length and width must be positive numbers.")

    def calculate_area(self):
        self.validate_dimensions()
        return self.length * self.width

if __name__ == '__main__':
    try:
        rectangle = Rectangle(25, 15)
        area = rectangle.calculate_area()
        print(area)
    except ValueError as e:
        print(e)