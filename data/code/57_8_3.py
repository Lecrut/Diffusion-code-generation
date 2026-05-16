class AreaCalculator:
    def __init__(self):
        self.area_formulas = {
            'square': lambda side: side * side,
            'rectangle': lambda length, width: length * width,
            'circle': lambda radius: 3.14159 * radius * radius,
            'triangle': lambda base, height: 0.5 * base * height
        }
    def calculate_area(self, shape, **kwargs):
        if shape not in self.area_formulas:
            raise ValueError(f"Unknown shape: {shape}")
        formula = self.area_formulas[shape]
        if shape == 'square':
            if 'side' not in kwargs:
                raise ValueError("Missing 'side' for square")
            return formula(kwargs['side'])
        elif shape == 'rectangle':
            if 'length' not in kwargs or 'width' not in kwargs:
                raise ValueError("Missing 'length' and 'width' for rectangle")
            return formula(kwargs['length'], kwargs['width'])
        elif shape == 'circle':
            if 'radius' not in kwargs:
                raise ValueError("Missing 'radius' for circle")
            return formula(kwargs['radius'])
        elif shape == 'triangle':
            if 'base' not in kwargs or 'height' not in kwargs:
                raise ValueError("Missing 'base' and 'height' for triangle")
            return formula(kwargs['base'], kwargs['height'])
        else:
            return None
if __name__ == '__main__':
    calculator = AreaCalculator()
    square_area = calculator.calculate_area('square', side=5)
    print(f"Area of square (side=5): {square_area}")
    circle_area = calculator.calculate_area('circle', radius=4)
    print(f"Area of circle (radius=4): {circle_area}")
    rectangle_area = calculator.calculate_area('rectangle', length=10, width=3)
    print(f"Area of rectangle (length=10, width=3): {rectangle_area}")
    triangle_area = calculator.calculate_area('triangle', base=6, height=4)
    print(f"Area of triangle (base=6, height=4): {triangle_area}")
    try:
        calculator.calculate_area('pentagon', side=5)
    except ValueError as e:
        print(f"Error caught: {e}")