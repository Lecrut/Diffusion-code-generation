class GeometryUtils:
    @staticmethod
    def calculate_perimeter(shape, *dimensions):
        if shape == 'rectangle':
            if len(dimensions) != 2:
                raise ValueError("Rectangle requires exactly two dimensions: length and width.")
            length, width = dimensions
            return 2 * (length + width)
        elif shape == 'circle':
            if len(dimensions) != 1:
                raise ValueError("Circle requires exactly one dimension: radius.")
            radius = dimensions[0]
            return 2 * 3.14159 * radius
        elif shape == 'triangle':
            if len(dimensions) != 3:
                raise ValueError("Triangle requires exactly three dimensions: side1, side2, and side3.")
            side1, side2, side3 = dimensions
            return side1 + side2 + side3
        else:
            raise ValueError(f"Unsupported shape: {shape}")

if __name__ == '__main__':
    rectangle_perimeter = GeometryUtils.calculate_perimeter('rectangle', 5, 3)
    circle_perimeter = GeometryUtils.calculate_perimeter('circle', 7)
    triangle_perimeter = GeometryUtils.calculate_perimeter('triangle', 4, 5, 6)

    print(f"Rectangle Perimeter: {rectangle_perimeter}")
    print(f"Circle Perimeter: {circle_perimeter}")
    print(f"Triangle Perimeter: {triangle_perimeter}")