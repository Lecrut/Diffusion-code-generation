class Geometry:
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def calculate_area(self, shape_type):
        if shape_type == 'triangle':
            base = self.dimensions.get('base', 0)
            height = self.dimensions.get('height', 0)
            return 0.5 * base * height
        raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    sample_dimensions = {'base': 6, 'height': 8}
    geometry = Geometry(sample_dimensions)
    try:
        area = geometry.calculate_area('triangle')
        print(area)
    except ValueError as e:
        print(e)