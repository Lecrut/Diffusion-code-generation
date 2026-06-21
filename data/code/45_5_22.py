class GeometryUtils:
    @staticmethod
    def calculate_area(shape, *dimensions):
        if shape == 'rectangle':
            if len(dimensions) != 2:
                raise ValueError("Rectangle requires exactly two dimensions: width and height.")
            return dimensions[0] * dimensions[1]
        elif shape == 'circle':
            if len(dimensions) != 1:
                raise ValueError("Circle requires exactly one dimension: radius.")
            import math
            return math.pi * (dimensions[0] ** 2)
        else:
            raise ValueError(f"Unsupported shape: {shape}")

if __name__ == '__main__':
    rectangle_area = GeometryUtils.calculate_area('rectangle', 5, 10)
    circle_area = GeometryUtils.calculate_area('circle', 7)

    print("Rectangle Area:", rectangle_area)
    print("Circle Area:", circle_area)