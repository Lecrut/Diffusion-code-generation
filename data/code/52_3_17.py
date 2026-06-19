import math

class ShapeCalculator:
    def __init__(self):
        self.shapes = {
            'rectangle': self.calculate_rectangle_area,
            'circle': self.calculate_circle_area,
            'triangle': self.calculate_triangle_area
        }

    def calculate_rectangle_area(self, length, width):
        return length * width

    def calculate_circle_area(self, radius):
        return math.pi * (radius ** 2)

    def calculate_triangle_area(self, base, height):
        return 0.5 * base * height

    def calculate_area(self, shape, *args):
        if shape in self.shapes:
            return self.shapes[shape](*args)
        else:
            raise ValueError("Unsupported shape")

if __name__ == '__main__':
    calculator = ShapeCalculator()
    rectangle_area = calculator.calculate_area('rectangle', 5, 3)
    circle_area = calculator.calculate_area('circle', 4)
    triangle_area = calculator.calculate_area('triangle', 6, 2)
    print(f"Rectangle area: {rectangle_area}")
    print(f"Circle area: {circle_area}")
    print(f"Triangle area: {triangle_area}")