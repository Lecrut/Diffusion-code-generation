from typing import Union

class AreaCalculator:
    def __init__(self):
        self.shapes = {
            'square': self.calculate_square_area,
            'rectangle': self.calculate_rectangle_area,
            'circle': self.calculate_circle_area,
            'triangle': self.calculate_triangle_area
        }

    def calculate_square_area(self, side_length: float) -> float:
        if side_length < 0:
            raise ValueError("Side length cannot be negative")
        return side_length ** 2

    def calculate_rectangle_area(self, length: float, width: float) -> float:
        if length < 0 or width < 0:
            raise ValueError("Length and width cannot be negative")
        return length * width

    def calculate_circle_area(self, radius: float) -> float:
        import math
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return math.pi * radius ** 2

    def calculate_triangle_area(self, base: float, height: float) -> float:
        if base < 0 or height < 0:
            raise ValueError("Base and height cannot be negative")
        return 0.5 * base * height

    def calculate_area(self, shape_type: str, **kwargs) -> Union[float, None]:
        shape_function = self.shapes.get(shape_type)
        if shape_function:
            return shape_function(**kwargs)
        return None

if __name__ == '__main__':
    calculator = AreaCalculator()
    square_side = 4.0
    rectangle_length = 5.0
    rectangle_width = 3.0
    circle_radius = 7.0
    triangle_base = 6.0
    triangle_height = 4.0

    print("Area of Square:", calculator.calculate_area('square', side_length=square_side))
    print("Area of Rectangle:", calculator.calculate_area('rectangle', length=rectangle_length, width=rectangle_width))
    print("Area of Circle:", calculator.calculate_area('circle', radius=circle_radius))
    print("Area of Triangle:", calculator.calculate_area('triangle', base=triangle_base, height=triangle_height))