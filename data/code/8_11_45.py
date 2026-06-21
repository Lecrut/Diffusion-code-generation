class ShapeScaler:
    def __init__(self, shapes):
        self.shapes = shapes

    def scale_areas(self, scale_factor):
        return [shape['width'] * shape['height'] * scale_factor for shape in self.shapes]

if __name__ == '__main__':
    shapes = [
        {'width': 3, 'height': 4},
        {'width': 5, 'height': 6},
        {'width': 7, 'height': 8}
    ]
    scaler = ShapeScaler(shapes)
    scale_factor = 2
    scaled_areas = scaler.scale_areas(scale_factor)
    print(scaled_areas)