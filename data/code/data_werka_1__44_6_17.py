PERIMETER_FACTOR = 2

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_perimeter(self):
        return PERIMETER_FACTOR * (self.length + self.width)

if __name__ == '__main__':
    rect = Rectangle(10, 6)
    print(rect.calculate_perimeter())