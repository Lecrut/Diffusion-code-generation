import math

class GeometryCalculator:
    @staticmethod
    def rectangle_area(length, width):
        return length * width

    @staticmethod
    def circle_area(radius):
        return math.pi * radius ** 2

    @staticmethod
    def triangle_area(base, height):
        return 0.5 * base * height

    @staticmethod
    def calculate_area(shape, *args):
        if shape == 'rectangle':
            return GeometryCalculator.rectangle_area(*args)
        elif shape == 'circle':
            return GeometryCalculator.circle_area(*args[0])
        elif shape == 'triangle':
            return GeometryCalculator.triangle_area(*args)
        else:
            raise ValueError("Unsupported shape")

if __name__ == '__main__':
    rectangle_area = GeometryCalculator.calculate_area('rectangle', 6, 4)
    circle_area = GeometryCalculator.calculate_area('circle', 5)
    triangle_area = GeometryCalculator.calculate_area('triangle', 7, 3)
    print(f"Rectangle Area: {rectangle_area}")
    print(f"Circle Area: {circle_area}")
    print(f"Triangle Area: {triangle_area}")