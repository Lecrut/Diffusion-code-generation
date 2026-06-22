class Rectangle:
    PERIMETER_MULTIPLIER = 2

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return self.PERIMETER_MULTIPLIER * (self.width + self.height)

if __name__ == '__main__':
    rect = Rectangle(5, 3)
    print(rect.calculate_perimeter())