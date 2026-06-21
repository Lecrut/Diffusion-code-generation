SHAPE_AREA_CALCULATORS = {
    'triangle': lambda base, height: 0.5 * base * height,
}

def calculate_area(shape_type, base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers")
    
    area_calculator = SHAPE_AREA_CALCULATORS.get(shape_type)
    if not area_calculator:
        raise ValueError(f"Unsupported shape type: {shape_type}")
    
    return area_calculator(base, height)

if __name__ == '__main__':
    base = 12
    height = 3.5
    shape_type = 'triangle'
    area = calculate_area(shape_type, base, height)
    print(area)