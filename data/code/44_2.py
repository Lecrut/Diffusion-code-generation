class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
if __name__ == '__main__':
    rect = Rectangle(10, 5)
    perimeter = rect.calculate_perimeter()
    print(perimeter)