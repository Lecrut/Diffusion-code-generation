SHAPE_FORMULAS = {
    'square': lambda side: side * side,
    'rectangle': lambda length, width: length * width,
}

def calculate_area(shape, base=None, height=None):
    if shape not in SHAPE_FORMULAS:
        raise ValueError(f"Unknown shape: {shape}")
    
    formula = SHAPE_FORMULAS[shape]
    if shape == 'square':
        return formula(base)
    elif shape == 'rectangle':
        return formula(base, height)

if __name__ == '__main__':
    square_area = calculate_area('square', base=5)
    rectangle_area = calculate_area('rectangle', base=4, height=6)
    
    print(f"Area of square: {square_area}")
    print(f"Area of rectangle: {rectangle_area}")