import math

class GeometryUtils:
    PI = math.pi

    @staticmethod
    def calculate_rectangle_area(length, width):
        return length * width

    @staticmethod
    def calculate_circle_area(radius):
        return GeometryUtils.PI * (radius ** 2)

    @staticmethod
    def calculate_triangle_area(base, height):
        return 0.5 * base * height

    @staticmethod
    def calculate_area(shape, *args):
        if shape == 'rectangle':
            if len(args) != 2:
                raise ValueError("Rectangle requires two arguments: length and width")
            return GeometryUtils.calculate_rectangle_area(*args)
        elif shape == 'circle':
            if len(args) != 1:
                raise ValueError("Circle requires one argument: radius")
            return GeometryUtils.calculate_circle_area(*args)
        elif shape == 'triangle':
            if len(args) != 2:
                raise ValueError("Triangle requires two arguments: base and height")
            return GeometryUtils.calculate_triangle_area(*args)
        else:
            raise ValueError("Unsupported shape")

if __name__ == '__main__':
    rectangle_area = GeometryUtils.calculate_area('rectangle', 6, 12)
    circle_area = GeometryUtils.calculate_area('circle', 8)
    triangle_area = GeometryUtils.calculate_area('triangle', 10, 5)

    print(f"Rectangle Area: {rectangle_area}")
    print(f"Circle Area: {circle_area}")
    print(f"Triangle Area: {triangle_area}")