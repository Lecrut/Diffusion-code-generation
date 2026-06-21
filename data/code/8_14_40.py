import math

class GeometryCalculator:
    def calculate_rectangle_area(self, length, width):
        return length * width

    def calculate_circle_area(self, radius):
        return math.pi * radius ** 2

    def calculate_triangle_area(self, base, height):
        return 0.5 * base * height

    def calculate_area(self, shape, *args):
        if shape == 'rectangle':
            if len(args) != 2:
                raise ValueError("Rectangle requires two arguments: length and width")
            return self.calculate_rectangle_area(*args)
        elif shape == 'circle':
            if len(args) != 1:
                raise ValueError("Circle requires one argument: radius")
            return self.calculate_circle_area(*args)
        elif shape == 'triangle':
            if len(args) != 2:
                raise ValueError("Triangle requires two arguments: base and height")
            return self.calculate_triangle_area(*args)
        else:
            raise ValueError("Unsupported shape")

if __name__ == '__main__':
    calculator = GeometryCalculator()
    
    rectangle_area = calculator.calculate_area('rectangle', 6, 4)
    circle_area = calculator.calculate_area('circle', 8)
    triangle_area = calculator.calculate_area('triangle', 10, 3)
    
    print(f"Rectangle Area: {rectangle_area}")
    print(f"Circle Area: {circle_area}")
    print(f"Triangle Area: {triangle_area}")