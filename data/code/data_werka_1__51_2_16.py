class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    rect1 = Rectangle(6, 4)
    perimeter1 = rect1.calculate_perimeter()
    print(perimeter1)
    rect2 = Rectangle(9, 3)
    perimeter2 = rect2.calculate_perimeter()
    print(perimeter2)