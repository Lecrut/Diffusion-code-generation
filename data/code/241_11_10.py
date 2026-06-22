class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers.")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

if __name__ == '__main__':
    rect = Rectangle(5, 10)
    print(f"Area: {rect.area()}")