class ShapeUtils:
    SHAPE_TYPES = {'rectangle': 4, 'square': 4, 'triangle': 3, 'circle': 1}

    @staticmethod
    def calculate_perimeter(shape_type, *dimensions):
        if shape_type not in ShapeUtils.SHAPE_TYPES:
            raise ValueError('Unsupported shape type')
        if shape_type == 'circle':
            return 2 * 3.14159 * dimensions[0]
        perimeter = sum(dimensions) * ShapeUtils.SHAPE_TYPES[shape_type] / len(dimensions)
        return perimeter
if __name__ == '__main__':
    rectangle_length = 5
    rectangle_width = 3
    square_side = 4
    triangle_side1 = 3
    triangle_side2 = 4
    triangle_side3 = 5
    circle_radius = 7
    rectangle_perimeter = ShapeUtils.calculate_perimeter('rectangle', rectangle_length, rectangle_width)
    square_perimeter = ShapeUtils.calculate_perimeter('square', square_side)
    triangle_perimeter = ShapeUtils.calculate_perimeter('triangle', triangle_side1, triangle_side2, triangle_side3)
    circle_perimeter = ShapeUtils.calculate_perimeter('circle', circle_radius)
    print(f'Rectangle Perimeter: {rectangle_perimeter}')
    print(f'Square Perimeter: {square_perimeter}')
    print(f'Triangle Perimeter: {triangle_perimeter}')
    print(f'Circle Perimeter: {circle_perimeter}')