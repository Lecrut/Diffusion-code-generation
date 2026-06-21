import math

class GeometryUtils:
    @staticmethod
    def calculate_area(shape, *args):
        if shape == 'rectangle':
            length = args[0]
            width = args[1]
            return GeometryUtils._calculate_rectangle_area(length, width)
        elif shape == 'circle':
            radius = args[0]
            return GeometryUtils._calculate_circle_area(radius)
        elif shape == 'triangle':
            base = args[0]
            height = args[1]
            return GeometryUtils._calculate_triangle_area(base, height)
        else:
            raise ValueError("Unsupported shape")

    @staticmethod
    def _calculate_rectangle_area(length, width):
        return length * width

    @staticmethod
    def _calculate_circle_area(radius):
        return math.pi * (radius ** 2)

    @staticmethod
    def _calculate_triangle_area(base, height):
        return 0.5 * base * height

if __name__ == '__main__':
    rectangle_length = 6
    rectangle_width = 4
    circle_radius = 3
    triangle_base = 7
    triangle_height = 2

    rectangle_area = GeometryUtils.calculate_area('rectangle', rectangle_length, rectangle_width)
    circle_area = GeometryUtils.calculate_area('circle', circle_radius)
    triangle_area = GeometryUtils.calculate_area('triangle', triangle_base, triangle_height)

    print(f"Rectangle Area: {rectangle_area}")
    print(f"Circle Area: {circle_area}")
    print(f"Triangle Area: {triangle_area}")