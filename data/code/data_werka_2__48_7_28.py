class Rectangle:
    def __init__(self, base, height):
        if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("Base and height must be numbers.")
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        self.base = base
        self.height = height

    def calculate_area(self):
        return self.base * self.height

if __name__ == '__main__':
    rect1 = Rectangle(5.5, 3.2)
    print(rect1.calculate_area())

    rect2 = Rectangle(7.8, 4.6)
    print(rect2.calculate_area())