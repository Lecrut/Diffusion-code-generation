class Shape:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width is not None else length

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

if __name__ == '__main__':
    square = Shape(5)
    rectangle = Shape(4, 6)
    
    print("Square Perimeter:", square.perimeter())
    print("Square Area:", square.area())
    print("Rectangle Perimeter:", rectangle.perimeter())
    print("Rectangle Area:", rectangle.area())