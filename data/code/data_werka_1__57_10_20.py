import math

class AreaCalculator:
    PI = math.pi
    
    @staticmethod
    def calculate_circle_area(radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return AreaCalculator.PI * radius ** 2
    
    @staticmethod
    def calculate_triangle_area(base, height):
        if base < 0 or height < 0:
            raise ValueError("Base and height cannot be negative")
        return 0.5 * base * height

if __name__ == '__main__':
    shape = 'circle'
    radius = 10
    area_circle = AreaCalculator.calculate_circle_area(radius)
    print(area_circle)
    
    shape = 'triangle'
    base = 6
    height = 8
    area_triangle = AreaCalculator.calculate_triangle_area(base, height)
    print(area_triangle)