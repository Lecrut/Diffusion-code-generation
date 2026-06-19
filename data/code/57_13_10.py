class GeometryCalculator:
    def __init__(self):
        self.shapes = {
            'triangle': {'base': 0, 'height': 0}
        }

    def set_triangle_dimensions(self, base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        self.shapes['triangle']['base'] = base
        self.shapes['triangle']['height'] = height

    def calculate_area(self, shape_type):
        if shape_type == 'triangle':
            base = self.shapes['triangle']['base']
            height = self.shapes['triangle']['height']
            return 0.5 * base * height
        else:
            raise ValueError("Unsupported shape type.")

if __name__ == '__main__':
    calculator = GeometryCalculator()
    try:
        calculator.set_triangle_dimensions(6, 8)
        area = calculator.calculate_area('triangle')
        print(area)
    except ValueError as e:
        print(e)