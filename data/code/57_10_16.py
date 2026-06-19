import math

class AreaCalculator:
    def __init__(self):
        self.shapes = {
            'circle': self.circle_area,
            'triangle': self.triangle_area
        }
    
    def calculate(self, shape, **kwargs):
        if shape not in self.shapes:
            raise ValueError("Unsupported shape")
        return self.shapes[shape](**kwargs)
    
    def circle_area(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return math.pi * radius ** 2
    
    def triangle_area(self, base, height):
        if base < 0 or height < 0:
            raise ValueError("Base and height cannot be negative")
        return 0.5 * base * height

if __name__ == '__main__':
    calculator = AreaCalculator()
    
    circle_radius = 10
    try:
        area_circle = calculator.calculate('circle', radius=circle_radius)
        print(f"Area of circle with radius {circle_radius}: {area_circle}")
    except ValueError as e:
        print(e)
    
    triangle_base = 8
    triangle_height = 6
    try:
        area_triangle = calculator.calculate('triangle', base=triangle_base, height=triangle_height)
        print(f"Area of triangle with base {triangle_base} and height {triangle_height}: {area_triangle}")
    except ValueError as e:
        print(e)