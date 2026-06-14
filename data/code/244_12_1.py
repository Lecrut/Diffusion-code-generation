class ShapeCalculator:
    def calculate_total_area(self, shapes):
        total_area = 0
        for shape in shapes:
            shape_type = shape.get('shape_type')
            dimensions = shape.get('dimensions', {})
            area = 0
            if shape_type == 'rectangle':
                length = dimensions.get('length', 0)
                width = dimensions.get('width', 0)
                area = length * width
            elif shape_type == 'circle':
                radius = dimensions.get('radius', 0)
                area = 3.14159 * (radius ** 2)
            elif shape_type == 'triangle':
                base = dimensions.get('base', 0)
                height = dimensions.get('height', 0)
                area = 0.5 * base * height
            else:
                continue
            total_area += area
        return total_area
if __name__ == '__main__':
    calculator = ShapeCalculator()
    shape_definitions = [
        {'shape_type': 'rectangle', 'dimensions': {'length': 10, 'width': 5}},
        {'shape_type': 'circle', 'dimensions': {'radius': 4}},
        {'shape_type': 'triangle', 'dimensions': {'base': 8, 'height': 6}},
        {'shape_type': 'square', 'dimensions': {'side': 7}}
    ]
    total = calculator.calculate_total_area(shape_definitions)
    print(total)