class GeometryUtils:
    @staticmethod
    def calculate_perimeter(shape, *dimensions):
        if shape == 'rectangle':
            if len(dimensions) != 2:
                raise ValueError("Rectangle requires exactly two dimensions: width and height.")
            width, height = dimensions
            return 2 * (width + height)
        elif shape == 'circle':
            if len(dimensions) != 1:
                raise ValueError("Circle requires exactly one dimension: radius.")
            radius = dimensions[0]
            return 2 * 3.14159 * radius
        else:
            raise ValueError(f"Unsupported shape: {shape}")

if __name__ == '__main__':
    rectangle_perimeter = GeometryUtils.calculate_perimeter('rectangle', 5, 10)
    circle_perimeter = GeometryUtils.calculate_perimeter('circle', 7)

    print("Rectangle Perimeter:", rectangle_perimeter)
    print("Circle Perimeter:", circle_perimeter)