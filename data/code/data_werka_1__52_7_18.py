import math

class ShapeCalculator:
    SHAPE_TYPES = {
        'rectangle': 2,
        'circle': 1,
        'triangle': 2
    }

    @staticmethod
    def calculate_area(shape_type, dimensions):
        if shape_type == 'rectangle':
            length, width = dimensions
            return length * width
        elif shape_type == 'circle':
            radius = dimensions[0]
            return math.pi * (radius ** 2)
        elif shape_type == 'triangle':
            base, height = dimensions
            return 0.5 * base * height
        else:
            raise ValueError("Unsupported shape type")

    @staticmethod
    def total_area_from_file(file_content):
        total_area = 0
        lines = file_content.strip().split('\n')
        for line in lines:
            parts = line.split(',')
            shape_type = parts[0].strip()
            dimensions = [float(part.strip()) for part in parts[1:]]
            if len(dimensions) != ShapeCalculator.SHAPE_TYPES.get(shape_type, 0):
                raise ValueError(f"Incorrect number of dimensions for {shape_type}")
            total_area += ShapeCalculator.calculate_area(shape_type, dimensions)
        return total_area

if __name__ == '__main__':
    sample_file_content = """rectangle,3.0,4.0
circle,5.0
triangle,6.0,8.0"""
    print(ShapeCalculator.total_area_from_file(sample_file_content))