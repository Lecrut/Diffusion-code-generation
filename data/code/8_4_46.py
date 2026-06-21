import math

class Shape:
    PI = 3.14159

    @staticmethod
    def calculate_area(shape_type, dimensions):
        if shape_type == 'rectangle':
            length, width = dimensions
            return length * width
        elif shape_type == 'circle':
            radius = dimensions[0]
            return Shape.PI * radius * radius
        else:
            raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    rectangle_area = Shape.calculate_area('rectangle', (9, 3))
    circle_area = Shape.calculate_area('circle', (4,))
    print(rectangle_area)
    print(circle_area)