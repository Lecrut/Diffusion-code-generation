class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def display_dimensions(self):
        return f"Length: {self.length}, Width: {self.width}"

if __name__ == '__main__':
    rect = Rectangle(6, 4)
    print(rect.display_dimensions())
    perimeter = rect.calculate_perimeter()
    print(f"Perimeter: {perimeter}")