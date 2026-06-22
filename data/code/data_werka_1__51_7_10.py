class MeasurementUtils:
    PERIMETER_FORMULAS = {
        'rectangle': lambda l, w: 2 * (l + w),
        'square': lambda s: 4 * s,
        'triangle': lambda a, b, c: a + b + c,
        'circle': lambda r: 2 * 3.14159 * r
    }

    @staticmethod
    def calculate_perimeter(shape_type, *dimensions):
        if shape_type not in MeasurementUtils.PERIMETER_FORMULAS:
            raise ValueError('Unsupported shape type')
        return MeasurementUtils.PERIMETER_FORMULAS[shape_type](*dimensions)

if __name__ == '__main__':
    rectangle_length = 5
    rectangle_width = 3
    square_side = 4
    triangle_side1 = 3
    triangle_side2 = 4
    triangle_side3 = 5
    circle_radius = 7

    try:
        print(MeasurementUtils.calculate_perimeter('rectangle', rectangle_length, rectangle_width))
        print(MeasurementUtils.calculate_perimeter('square', square_side))
        print(MeasurementUtils.calculate_perimeter('triangle', triangle_side1, triangle_side2, triangle_side3))
        print(MeasurementUtils.calculate_perimeter('circle', circle_radius))
    except ValueError as e:
        print(e)