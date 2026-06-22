class ShapeAreaCalculator:
    PI = 3.141592653589793

    @staticmethod
    def calculate_rectangle_area(length, width):
        return length * width

    @staticmethod
    def calculate_circle_area(radius):
        return ShapeAreaCalculator.PI * radius ** 2

    def calculate_area(self, shape_type, dimensions):
        if shape_type.lower() == 'rectangle':
            if len(dimensions) != 2:
                raise ValueError('Rectangle requires two dimensions: length and width.')
            return self.calculate_rectangle_area(*dimensions)
        elif shape_type.lower() == 'circle':
            if len(dimensions) != 1:
                raise ValueError('Circle requires one dimension: radius.')
            return self.calculate_circle_area(dimensions[0])
        else:
            raise ValueError('Unsupported shape type.')
if __name__ == '__main__':
    calculator = ShapeAreaCalculator()
    rect_area = calculator.calculate_area('rectangle', (5, 3))
    print(f'Rectangle area with dimensions 5x3 is: {rect_area}')
    circle_area = calculator.calculate_area('circle', (7,))
    print(f'Circle area with radius 7 is: {circle_area}')