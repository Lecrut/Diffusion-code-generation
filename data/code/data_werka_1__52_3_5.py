import math

class ShapeAreaCalculator:
    @staticmethod
    def calculate_rectangle_area(length, width):
        return length * width

    @staticmethod
    def calculate_circle_area(radius):
        return math.pi * (radius ** 2)

    @staticmethod
    def calculate_triangle_area(base, height):
        return 0.5 * base * height

    @staticmethod
    def calculate_area(shape, *args):
        if shape == 'rectangle':
            length, width = args
            return ShapeAreaCalculator.calculate_rectangle_area(length, width)
        elif shape == 'circle':
            radius = args[0]
            return ShapeAreaCalculator.calculate_circle_area(radius)
        elif shape == 'triangle':
            base, height = args
            return ShapeAreaCalculator.calculate_triangle_area(base, height)
        else:
            raise ValueError("Unsupported shape")

if __name__ == '__main__':
    rectangle_area = ShapeAreaCalculator.calculate_area('rectangle', 5, 3)
    circle_area = ShapeAreaCalculator.calculate_area('circle', 7)
    triangle_area = ShapeAreaCalculator.calculate_area('triangle', 4, 6)
    print(f"Rectangle area: {rectangle_area}")
    print(f"Circle area: {circle_area}")
    print(f"Triangle area: {triangle_area}")