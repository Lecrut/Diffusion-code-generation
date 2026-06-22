class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers.")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

if __name__ == '__main__':
    rect1 = Rectangle(5, 10)
    print(f"Area of rectangle: {rect1.area()}")

    try:
        rect2 = Rectangle(-5, 10)
    except ValueError as e:
        print(f"Error caught: {e}")

    try:
        rect3 = Rectangle(5, 0)
    except ValueError as e:
        print(f"Error caught: {e}")

    rect4 = Rectangle(3.5, 2)
    print(f"Area of rectangle: {rect4.area()}")