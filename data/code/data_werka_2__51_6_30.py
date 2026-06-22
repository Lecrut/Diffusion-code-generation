class GeometryUtils:
    SHAPE_FORMULAS = {
        'rectangle': lambda length, width: 2 * (length + width),
        'circle': lambda radius: 2 * 3.14159 * radius,
    }

    @staticmethod
    def calculate_perimeter(shape, *dimensions):
        if shape not in GeometryUtils.SHAPE_FORMULAS:
            raise ValueError(f"Unsupported shape: {shape}")
        
        formula = GeometryUtils.SHAPE_FORMULAS[shape]
        return formula(*dimensions)

if __name__ == '__main__':
    rectangle_perimeter = GeometryUtils.calculate_perimeter('rectangle', 5, 3)
    circle_perimeter = GeometryUtils.calculate_perimeter('circle', 7)

    print(f"Rectangle Perimeter: {rectangle_perimeter}")
    print(f"Circle Perimeter: {circle_perimeter}")