class PerimeterCalculator:
    PERIMETER_FORMULAS = {
        'rectangle': lambda l, w: 2 * (l + w),
        'square': lambda s: 4 * s,
        'triangle': lambda a, b, c: a + b + c,
        'circle': lambda r: 2 * 3.14159 * r
    }

    @staticmethod
    def calculate_perimeter(shape_type, *dimensions):
        if shape_type not in PerimeterCalculator.PERIMETER_FORMULAS:
            raise ValueError('Unsupported shape type')
        return PerimeterCalculator.PERIMETER_FORMULAS[shape_type](*dimensions)

if __name__ == '__main__':
    rectangle_length = 5
    rectangle_width = 3
    square_side = 4
    triangle_side1 = 3
    triangle_side2 = 4
    triangle_side3 = 5
    circle_radius = 7

    try:
        perimeter_rectangle = PerimeterCalculator.calculate_perimeter('rectangle', rectangle_length, rectangle_width)
        perimeter_square = PerimeterCalculator.calculate_perimeter('square', square_side)
        perimeter_triangle = PerimeterCalculator.calculate_perimeter('triangle', triangle_side1, triangle_side2, triangle_side3)
        perimeter_circle = PerimeterCalculator.calculate_perimeter('circle', circle_radius)

        print(f"Rectangle Perimeter: {perimeter_rectangle}")
        print(f"Square Perimeter: {perimeter_square}")
        print(f"Triangle Perimeter: {perimeter_triangle}")
        print(f"Circle Perimeter: {perimeter_circle}")

    except ValueError as e:
        print(e)