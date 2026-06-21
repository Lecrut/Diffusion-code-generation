import math

class GeometryCalculator:
    def calculate_rectangle_area(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers")
        return length * width

    def calculate_circle_area(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive number")
        return math.pi * radius ** 2

    def calculate_triangle_area(self, base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers")
        return 0.5 * base * height

if __name__ == '__main__':
    calculator = GeometryCalculator()
    
    try:
        rectangle_area = calculator.calculate_rectangle_area(6, 4)
        print(f"Rectangle Area: {rectangle_area}")
        
        circle_area = calculator.calculate_circle_area(3)
        print(f"Circle Area: {circle_area}")
        
        triangle_area = calculator.calculate_triangle_area(10, 2)
        print(f"Triangle Area: {triangle_area}")
    except ValueError as e:
        print(e)