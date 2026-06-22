SHAPE_FORMULAS = {'triangle': lambda base, height: 0.5 * base * height}

def calculate_area(shape_type, base, height):
    area_calculator = SHAPE_FORMULAS.get(shape_type)
    if not area_calculator:
        raise ValueError(f'Unsupported shape type: {shape_type}')
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise ValueError('Base and height must be numbers')
    if base <= 0 or height <= 0:
        raise ValueError('Base and height must be positive numbers')
    return area_calculator(base, height)
if __name__ == '__main__':
    base = 12.0
    height = 3.5
    shape_type = 'triangle'
    area = calculate_area(shape_type, base, height)
    print(area)