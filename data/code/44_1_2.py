class Rectangle:
    def __init__(self, length, width):
        if not (isinstance(length, (int, float)) and length > 0 and isinstance(width, (int, float)) and width > 0):
            raise ValueError("Length and width must be positive numbers.")
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    dimensions = {'length': 7, 'width': 4}
    rect = Rectangle(dimensions['length'], dimensions['width'])
    print(rect.perimeter())