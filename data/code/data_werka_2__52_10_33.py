class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == '__main__':
    try:
        rectangle = Rectangle(18, 6)
        area = rectangle.calculate_area()
        perimeter = rectangle.perimeter()
        print(f"Area: {area}")
        print(f"Perimeter: {perimeter}")
    except ValueError as e:
        print(e)