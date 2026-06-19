class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers.")
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

if __name__ == '__main__':
    try:
        rect1 = Rectangle(8, 5)
        perimeter1 = rect1.calculate_perimeter()
        print(f"Perimeter of Rectangle 1: {perimeter1}")

        rect2 = Rectangle(12, 7)
        perimeter2 = rect2.calculate_perimeter()
        print(f"Perimeter of Rectangle 2: {perimeter2}")
    except ValueError as e:
        print(e)