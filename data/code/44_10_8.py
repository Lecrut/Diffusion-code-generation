class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def display_dimensions(self):
        return f"Length: {self.length}, Width: {self.width}"

if __name__ == '__main__':
    rectangle = Rectangle(9, 5)
    print(rectangle.calculate_perimeter())
    print(rectangle.display_dimensions())