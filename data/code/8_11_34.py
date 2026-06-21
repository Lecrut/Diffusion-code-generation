class ShapeAreaCalculator:
    @staticmethod
    def calculate_area(shape):
        return shape['width'] * shape['height']

def scale_areas(shapes, scale_factor):
    return [ShapeAreaCalculator.calculate_area(shape) * scale_factor for shape in shapes]

if __name__ == '__main__':
    shapes = [
        {'width': 2, 'height': 3},
        {'width': 4, 'height': 5},
        {'width': 6, 'height': 7}
    ]
    scale_factor = 2
    scaled_areas = scale_areas(shapes, scale_factor)
    print(scaled_areas)