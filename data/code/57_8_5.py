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
                raise ValueError("Square requires 'side'")
            return formula(kwargs['side'])
        elif shape == 'rectangle':
            if 'length' not in kwargs or 'width' not in kwargs:
                raise ValueError("Rectangle requires 'length' and 'width'")
            return formula(kwargs['length'], kwargs['width'])
        elif shape == 'circle':
            if 'radius' not in kwargs:
                raise ValueError("Circle requires 'radius'")
            return formula(kwargs['radius'])
        elif shape == 'triangle':
            if 'base' not in kwargs or 'height' not in kwargs:
                raise ValueError("Triangle requires 'base' and 'height'")
            return formula(kwargs['base'], kwargs['height'])
        else:
            return None
if __name__ == '__main__':
    calculator = AreaCalculator()
    print("Square Area:")
    try:
        area_square = calculator.calculate_area('square', side=5)
        print(f"Area of square with side 5: {area_square}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\nCircle Area:")
    try:
        area_circle = calculator.calculate_area('circle', radius=4)
        print(f"Area of circle with radius 4: {area_circle}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\nRectangle Area:")
    try:
        area_rectangle = calculator.calculate_area('rectangle', length=10, width=3)
        print(f"Area of rectangle with length 10 and width 3: {area_rectangle}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\nTriangle Area:")
    try:
        area_triangle = calculator.calculate_area('triangle', base=6, height=4)
        print(f"Area of triangle with base 6 and height 4: {area_triangle}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\nUnknown Shape Test:")
    try:
        calculator.calculate_area('pentagon', side=5)
    except ValueError as e:
        print(f"Caught expected error: {e}")