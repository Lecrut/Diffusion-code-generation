import math

class GeometryCalculator:
    RECTANGLE_AREA = lambda width, height: width * height
    CIRCLE_AREA = lambda radius: math.pi * (radius ** 2)

    @staticmethod
    def calculate_scaled_area(shape, dimensions, scale_factor):
        if shape == 'rectangle':
            area = GeometryCalculator.RECTANGLE_AREA(*dimensions)
        elif shape == 'circle':
            area = GeometryCalculator.CIRCLE_AREA(dimensions[0])
        else:
            raise ValueError("Unsupported shape")
        return area * scale_factor

if __name__ == '__main__':
    rectangle_dimensions = (5, 10)
    circle_dimensions = (7,)
    scale_factor = 2.5
    rectangle_scaled_area = GeometryCalculator.calculate_scaled_area('rectangle', rectangle_dimensions, scale_factor)
    circle_scaled_area = GeometryCalculator.calculate_scaled_area('circle', circle_dimensions, scale_factor)
    print(rectangle_scaled_area)
    print(circle_scaled_area)