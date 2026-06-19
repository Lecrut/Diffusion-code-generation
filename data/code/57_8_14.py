class ShapeAreaCalculator:
    def __init__(self):
        self.shapes = {
            'triangle': lambda base, height: 0.5 * base * height,
            'rectangle': lambda length, width: length * width,
            'circle': lambda radius: 3.14159 * (radius ** 2),
            'square': lambda side: side * side
        }

    def calculate_area(self, shape, **kwargs):
        if shape not in self.shapes:
            raise ValueError(f"Unsupported shape: {shape}")
        
        formula = self.shapes[shape]
        try:
            return formula(**kwargs)
        except KeyError as e:
            missing_argument = str(e).split("'")[1]
            raise ValueError(f"Missing argument for {shape}: {missing_argument}")

if __name__ == '__main__':
    calculator = ShapeAreaCalculator()
    
    triangle_area = calculator.calculate_area('triangle', base=5, height=10)
    rectangle_area = calculator.calculate_area('rectangle', length=4, width=6)
    circle_area = calculator.calculate_area('circle', radius=3)
    square_area = calculator.calculate_area('square', side=7)

    print("Triangle Area:", triangle_area)
    print("Rectangle Area:", rectangle_area)
    print("Circle Area:", circle_area)
    print("Square Area:", square_area)