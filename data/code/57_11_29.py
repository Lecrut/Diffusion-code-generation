class Geometry:
    def __init__(self):
        self.shapes = {
            'triangle': {'base': 6, 'height': 8}
        }

    def calculate_area(self, shape_name):
        if shape_name not in self.shapes:
            raise ValueError("Unsupported shape.")
        
        shape = self.shapes[shape_name]
        base = shape['base']
        height = shape['height']
        return 0.5 * base * height

if __name__ == '__main__':
    geometry = Geometry()
    try:
        area = geometry.calculate_area('triangle')
        print(area)
    except ValueError as e:
        print(e)