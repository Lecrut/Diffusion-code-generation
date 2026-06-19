import math

class ShapeAreaCalculator:
    @staticmethod
    def square_area(side_length):
        return side_length ** 2

    @staticmethod
    def rectangle_area(length, width):
        return length * width

    @staticmethod
    def circle_area(radius):
        return math.pi * radius ** 2

def area_calculator(shape_type, dimensions):
    if shape_type == 'square':
        return ShapeAreaCalculator.square_area(dimensions['side_length'])
    elif shape_type == 'rectangle':
        return ShapeAreaCalculator.rectangle_area(dimensions['length'], dimensions['width'])
    elif shape_type == 'circle':
        return ShapeAreaCalculator.circle_area(dimensions['radius'])
    else:
        raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    square_dimensions = {'side_length': 5}
    rectangle_dimensions = {'length': 4, 'width': 3}
    circle_dimensions = {'radius': 2}

    print(area_calculator('square', square_dimensions))
    print(area_calculator('rectangle', rectangle_dimensions))
    print(area_calculator('circle', circle_dimensions))