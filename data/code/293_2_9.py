import math

class GeometryCalculator:
    def calculate_area(self, shape_type, **params):
        if shape_type == 'circle':
            return math.pi * params['radius'] ** 2
        elif shape_type == 'square':
            return params['side'] ** 2
        elif shape_type == 'rectangle':
            return params['length'] * params['width']
        else:
            raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    calculator = GeometryCalculator()
    circle_area = calculator.calculate_area('circle', radius=5)
    square_area = calculator.calculate_area('square', side=4)
    rectangle_area = calculator.calculate_area('rectangle', length=6, width=3)
    
    print(f"Circle area: {circle_area}")
    print(f"Square area: {square_area}")
    print(f"Rectangle area: {rectangle_area}")