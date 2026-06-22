class ShapeAreaCalculator:
    def __init__(self):
        self.formulas = {
            'triangle': lambda base, height: 0.5 * base * height,
            'rectangle': lambda length, width: length * width,
            'circle': lambda radius: 3.14159 * radius * radius
        }

    def calculate_area(self, shape, **kwargs):
        if shape not in self.formulas:
            raise ValueError(f"Unknown shape: {shape}")
        
        formula = self.formulas[shape]
        return formula(**kwargs)

if __name__ == '__main__':
    calculator = ShapeAreaCalculator()
    
    triangle_area = calculator.calculate_area('triangle', base=10, height=5)
    rectangle_area = calculator.calculate_area('rectangle', length=7, width=3)
    circle_area = calculator.calculate_area('circle', radius=6)

    print(f"Triangle Area: {triangle_area}")
    print(f"Rectangle Area: {rectangle_area}")
    print(f"Circle Area: {circle_area}")