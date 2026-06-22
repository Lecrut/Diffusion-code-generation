class ShapeAreaCalculator:
    def __init__(self, base, height):
        if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
            raise ValueError("Base and height must be numbers")
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers")
        self.base = base
        self.height = height

    def calculate_triangle_area(self):
        return 0.5 * self.base * self.height

def calculate_area(base, height):
    calculator = ShapeAreaCalculator(base, height)
    return calculator.calculate_triangle_area()

if __name__ == '__main__':
    base = 9
    height = 3
    area = calculate_area(base, height)
    print(area)