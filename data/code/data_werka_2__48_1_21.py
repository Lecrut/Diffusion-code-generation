class Shape:
    def __init__(self, length, width=None):
        self.length = length
        if width is None:
            self.width = length
        else:
            self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

if __name__ == '__main__':
    side_length_square = 8
    square = Shape(side_length_square)
    length_rectangle = 5
    width_rectangle = 10
    rectangle = Shape(length_rectangle, width_rectangle)
    
    print("Square Perimeter:", square.perimeter())
    print("Square Area:", square.area())
    print("Rectangle Perimeter:", rectangle.perimeter())
    print("Rectangle Area:", rectangle.area())