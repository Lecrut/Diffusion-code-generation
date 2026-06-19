class PerimeterCalculator:
    SHAPE_CONFIG = {
        'rectangle': {'sides': 2},
        'square': {'sides': 1},
        'triangle': {'sides': 3},
        'circle': {'sides': 0}
    }

    @staticmethod
    def calculate_perimeter(shape_type, *dimensions):
        if shape_type not in PerimeterCalculator.SHAPE_CONFIG:
            raise ValueError('Unsupported shape type')
        
        config = PerimeterCalculator.SHAPE_CONFIG[shape_type]
        if shape_type == 'circle':
            return 2 * 3.14159 * dimensions[0]
        
        perimeter = sum(dimensions) * config['sides']
        return perimeter

if __name__ == '__main__':
    rectangle_length = 5
    rectangle_width = 3
    square_side = 4
    triangle_side1 = 3
    triangle_side2 = 4
    triangle_side3 = 5
    circle_radius = 7

    try:
        print("Rectangle Perimeter:", PerimeterCalculator.calculate_perimeter('rectangle', rectangle_length, rectangle_width))
        print("Square Perimeter:", PerimeterCalculator.calculate_perimeter('square', square_side))
        print("Triangle Perimeter:", PerimeterCalculator.calculate_perimeter('triangle', triangle_side1, triangle_side2, triangle_side3))
        print("Circle Perimeter:", PerimeterCalculator.calculate_perimeter('circle', circle_radius))
    except ValueError as e:
        print(e)