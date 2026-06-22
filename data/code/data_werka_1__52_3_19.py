import math

class ShapeCalculator:
    def calculate_area(self, shape, *args):
        if shape == 'rectangle':
            length, width = args
            return self._calculate_rectangle_area(length, width)
        elif shape == 'circle':
            radius = args[0]
            return self._calculate_circle_area(radius)
        elif shape == 'triangle':
            base, height = args
            return self._calculate_triangle_area(base, height)
        else:
            raise ValueError("Unsupported shape")

    def _calculate_rectangle_area(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers")
        return length * width

    def _calculate_circle_area(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive number")
        return math.pi * (radius ** 2)

    def _calculate_triangle_area(self, base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers")
        return 0.5 * base * height

if __name__ == '__main__':
    calculator = ShapeCalculator()
    
    rectangle_area = calculator.calculate_area('rectangle', 5, 3)
    circle_area = calculator.calculate_area('circle', 4)
    triangle_area = calculator.calculate_area('triangle', 6, 2)
    
    print(f"Rectangle area: {rectangle_area}")
    print(f"Circle area: {circle_area}")
    print(f"Triangle area: {triangle_area}")