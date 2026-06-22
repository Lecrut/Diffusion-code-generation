class GeometryUtils:
    @staticmethod
    def calculate_area(shape, *args):
        if shape == 'rectangle':
            if len(args) != 2:
                raise ValueError("Rectangle requires two arguments: width and height")
            return args[0] * args[1]
        elif shape == 'circle':
            if len(args) != 1:
                raise ValueError("Circle requires one argument: radius")
            import math
            return math.pi * (args[0] ** 2)
        elif shape == 'triangle':
            if len(args) != 3:
                raise ValueError("Triangle requires three arguments: base and height")
            return 0.5 * args[0] * args[1]
        else:
            raise ValueError(f"Unsupported shape: {shape}")

if __name__ == '__main__':
    rectangle_area = GeometryUtils.calculate_area('rectangle', 5, 10)
    circle_area = GeometryUtils.calculate_area('circle', 7)
    triangle_area = GeometryUtils.calculate_area('triangle', 8, 4)

    print(f"Rectangle Area: {rectangle_area}")
    print(f"Circle Area: {circle_area}")
    print(f"Triangle Area: {triangle_area}")