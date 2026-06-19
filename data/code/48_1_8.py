class Shape:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width is not None else length

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def calculate_area(self):
        return self.length * self.width

if __name__ == '__main__':
    side_length_square = 7
    square = Shape(side_length_square)
    
    length_rectangle = 3
    width_rectangle = 9
    rectangle = Shape(length_rectangle, width_rectangle)
    
    print("Square Perimeter:", square.calculate_perimeter())
    print("Square Area:", square.calculate_area())
    print("Rectangle Perimeter:", rectangle.calculate_perimeter())
    print("Rectangle Area:", rectangle.calculate_area())