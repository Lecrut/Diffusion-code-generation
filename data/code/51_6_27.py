class GeometryUtils:
    PI = 3.14159

    @staticmethod
    def calculate_perimeter(shape, *dimensions):
        if shape == 'rectangle':
            return GeometryUtils._calculate_rectangle_perimeter(*dimensions)
        elif shape == 'circle':
            return GeometryUtils._calculate_circle_perimeter(*dimensions)
        else:
            raise ValueError(f'Unsupported shape: {shape}')

    @staticmethod
    def _calculate_rectangle_perimeter(length, width):
        if length <= 0 or width <= 0:
            raise ValueError('Length and width must be positive numbers.')
        return 2 * (length + width)

    @staticmethod
    def _calculate_circle_perimeter(radius):
        if radius <= 0:
            raise ValueError('Radius must be a positive number.')
        return 2 * GeometryUtils.PI * radius
if __name__ == '__main__':
    try:
        rectangle_perimeter = GeometryUtils.calculate_perimeter('rectangle', 5, 3)
        print(f'Rectangle Perimeter: {rectangle_perimeter}')
        circle_perimeter = GeometryUtils.calculate_perimeter('circle', 7)
        print(f'Circle Perimeter: {circle_perimeter}')
        invalid_rectangle_perimeter = GeometryUtils.calculate_perimeter('rectangle', -5, 3)
    except ValueError as e:
        print(e)
    try:
        invalid_circle_perimeter = GeometryUtils.calculate_perimeter('circle', -7)
    except ValueError as e:
        print(e)