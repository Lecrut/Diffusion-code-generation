SHAPE_CONFIG = {
    'triangle': {'factor': 0.5},
}

def calculate_area(shape_type, base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers")
    
    config = SHAPE_CONFIG.get(shape_type)
    if not config:
        raise ValueError(f"Unsupported shape type: {shape_type}")
    
    return config['factor'] * base * height

if __name__ == '__main__':
    base = 12
    height = 7
    shape_type = 'triangle'
    area = calculate_area(shape_type, base, height)
    print(area)