class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
if __name__ == '__main__':
    rect1 = Rectangle(10, 5)
    perimeter1 = rect1.calculate_perimeter()
    print(f"Perimeter of rectangle 1: {perimeter1}")
    rect2 = Rectangle(7, 3)
    perimeter2 = rect2.calculate_perimeter()
    print(f"Perimeter of rectangle 2: {perimeter2}")