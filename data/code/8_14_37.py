import math

class ShapeCalculator:
    SHAPE_FUNCTIONS = {
        'rectangle': lambda length, width: length * width,
        'circle': lambda radius: math.pi * radius ** 2,
        'triangle': lambda base, height: 0.5 * base * height
    }

    def calculate_area(self, shape, *args):
        if shape in self.SHAPE_FUNCTIONS:
            return self.SHAPE_FUNCTIONS[shape](*args)
        else:
            raise ValueError("Unsupported shape")

if __name__ == '__main__':
    calculator = ShapeCalculator()
    
    rectangle_area = calculator.calculate_area('rectangle', 5, 10)
    circle_area = calculator.calculate_area('circle', 7)
    triangle_area = calculator.calculate_area('triangle', 8, 6)
    
    print(f"Rectangle Area: {rectangle_area}")
    print(f"Circle Area: {circle_area}")
    print(f"Triangle Area: {triangle_area}")