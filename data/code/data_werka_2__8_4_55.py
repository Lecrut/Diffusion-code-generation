import math

class ShapeCalculator:
    PI = 3.14159

    @staticmethod
    def calculate_rectangle_area(length, width):
        return length * width

    @staticmethod
    def calculate_circle_area(radius):
        return ShapeCalculator.PI * radius * radius

def calculate_area(shape_type, dimensions):
    if shape_type == 'rectangle':
        length, width = dimensions
        return ShapeCalculator.calculate_rectangle_area(length, width)
    elif shape_type == 'circle':
        radius = dimensions[0]
        return ShapeCalculator.calculate_circle_area(radius)
    else:
        raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    rectangle_area = calculate_area('rectangle', (5, 10))
    circle_area = calculate_area('circle', (7,))
    print(rectangle_area)
    print(circle_area)