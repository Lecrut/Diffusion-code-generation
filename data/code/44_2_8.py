class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def calculate_area(self):
        return self.length * self.width

if __name__ == '__main__':
    rect = Rectangle(15, 8)
    perimeter = rect.calculate_perimeter()
    area = rect.calculate_area()
    print(f"Perimeter: {perimeter}")
    print(f"Area: {area}")