import math

class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers.")
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

def main():
    try:
        rect = Rectangle(5.0, 3.0)
        print(f"Perimeter: {rect.perimeter()}")
        print(f"Area: {rect.area()}")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()