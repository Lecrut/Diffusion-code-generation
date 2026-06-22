import math

class ShapeAreaCalculator:
    SHAPE_FUNCTIONS = {
        'rectangle': lambda width, height: width * height,
        'circle': lambda radius: math.pi * (radius ** 2)
    }

    @staticmethod
    def calculate_scaled_area(shape, dimensions, scale_factor):
        if shape not in ShapeAreaCalculator.SHAPE_FUNCTIONS:
            raise ValueError("Unsupported shape")
        area_calculator = ShapeAreaCalculator.SHAPE_FUNCTIONS[shape]
        area = area_calculator(*dimensions)
        return area * scale_factor

if __name__ == '__main__':
    rectangle_dimensions = (6, 12)
    circle_dimensions = (8,)
    scale_factor = 3.0
    rectangle_scaled_area = ShapeAreaCalculator.calculate_scaled_area('rectangle', rectangle_dimensions, scale_factor)
    circle_scaled_area = ShapeAreaCalculator.calculate_scaled_area('circle', circle_dimensions, scale_factor)
    print(f'Scaled area of the rectangle: {rectangle_scaled_area}')
    print(f'Scaled area of the circle: {circle_scaled_area}')