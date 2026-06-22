class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

if __name__ == '__main__':
    rect1 = Rectangle(3, 4)
    perimeter1 = rect1.calculate_perimeter()
    print(f"Perimeter of Rectangle 1: {perimeter1}")

    rect2 = Rectangle(7, 5)
    perimeter2 = rect2.calculate_perimeter()
    print(f"Perimeter of Rectangle 2: {perimeter2}")