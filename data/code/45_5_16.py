class GeometryUtils:
    @staticmethod
    def calculate_area(shape, *args):
        if shape == 'rectangle':
            return args[0] * args[1]
        elif shape == 'circle':
            import math
            return math.pi * (args[0] ** 2)
        elif shape == 'triangle':
            return 0.5 * args[0] * args[1]
        else:
            raise ValueError("Unsupported shape")

if __name__ == '__main__':
    rectangle_area = GeometryUtils.calculate_area('rectangle', 5, 3)
    circle_area = GeometryUtils.calculate_area('circle', 7)
    triangle_area = GeometryUtils.calculate_area('triangle', 4, 6)

    print(f"Rectangle Area: {rectangle_area}")
    print(f"Circle Area: {circle_area}")
    print(f"Triangle Area: {triangle_area}")