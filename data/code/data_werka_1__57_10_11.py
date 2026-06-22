import math

class AreaCalculator:
    def __init__(self):
        self.shapes = {
            'circle': self.circle_area,
            'triangle': self.triangle_area
        }
    
    def calculate(self, shape, **kwargs):
        try:
            return self.shapes[shape](**kwargs)
        except KeyError:
            raise ValueError("Invalid shape. Please choose 'circle' or 'triangle'.")
        except TypeError as e:
            raise ValueError(f"Missing arguments for {shape}: {e}")
    
    def circle_area(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        return math.pi * radius ** 2
    
    def triangle_area(self, base, height):
        if base < 0 or height < 0:
            raise ValueError("Base and height cannot be negative.")
        return 0.5 * base * height

if __name__ == '__main__':
    calculator = AreaCalculator()
    
    try:
        shape1 = 'circle'
        radius = 3
        area_circle = calculator.calculate(shape1, radius=radius)
        print(area_circle)
    except Exception as e:
        print(e)
    
    try:
        shape2 = 'triangle'
        base = 6
        height = 2
        area_triangle = calculator.calculate(shape2, base=base, height=height)
        print(area_triangle)
    except Exception as e:
        print(e)