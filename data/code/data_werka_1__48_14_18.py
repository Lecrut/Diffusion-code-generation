import math

class RightAngledTriangle:
    def __init__(self, base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        self.base = base
        self.height = height
        self.hypotenuse = self.calculate_hypotenuse()
        self.area = self.calculate_area()

    def calculate_hypotenuse(self):
        return math.sqrt(self.base ** 2 + self.height ** 2)

    def calculate_area(self):
        return (self.base * self.height) / 2

    def __str__(self):
        return f"Right-angled Triangle: Base={self.base}, Height={self.height}, Hypotenuse={self.hypotenuse:.2f}, Area={self.area:.2f}"

if __name__ == '__main__':
    try:
        triangle = RightAngledTriangle(6.0, 8.0)
        print(triangle)
    except ValueError as e:
        print(e)