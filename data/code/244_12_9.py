class Shape:
    @staticmethod
    def calculate_area(shape):
        shape_type = shape['shape_type']
        dimensions = shape['dimensions']
        if shape_type == 'triangle':
            return 0.5 * dimensions['base'] * dimensions['height']
        elif shape_type == 'trapezoid':
            return 0.5 * (dimensions['base1'] + dimensions['base2']) * dimensions['height']

class Main:
    @staticmethod
    def run():
        shapes = [
            {'shape_type': 'triangle', 'dimensions': {'base': 3, 'height': 4}},
            {'shape_type': 'trapezoid', 'dimensions': {'base1': 5, 'base2': 7, 'height': 8}}
        ]
        total_area = sum(Shape.calculate_area(shape) for shape in shapes)
        print(total_area)

if __name__ == '__main__':
    Main.run()