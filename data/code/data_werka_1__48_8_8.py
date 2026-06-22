class Rectangle:
    def __init__(self, base, height):
        if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
            raise ValueError("Base and height must be numbers.")
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        self.base = base
        self.height = height

    def calculate_area(self):
        return self.base * self.height

if __name__ == '__main__':
    try:
        rect = Rectangle(7.5, 3.1)
        area = rect.calculate_area()
        print(area)
    except ValueError as e:
        print(e)