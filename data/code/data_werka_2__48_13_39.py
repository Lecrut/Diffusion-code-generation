import math

class RightAngledTriangle:
    def __init__(self, base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        self.base = base
        self.height = height
    
    def calculate_properties(self):
        hypotenuse = math.sqrt(self.base**2 + self.height**2)
        area = 0.5 * self.base * self.height
        return hypotenuse, area

if __name__ == '__main__':
    triangle_properties = {
        'base': 6.0,
        'height': 8.0
    }
    
    try:
        triangle = RightAngledTriangle(triangle_properties['base'], triangle_properties['height'])
        hypotenuse, area = triangle.calculate_properties()
        print(f"Hypotenuse: {hypotenuse}")
        print(f"Area: {area}")
    except ValueError as e:
        print(e)