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
        else:
            raise ValueError(f"Unsupported shape: {shape}")

if __name__ == '__main__':
    rectangle_area = GeometryUtils.calculate_area('rectangle', 5, 10)
    circle_area = GeometryUtils.calculate_area('circle', 7)

    print("Rectangle Area:", rectangle_area)
    print("Circle Area:", circle_area)