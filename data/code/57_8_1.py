def calculate_area(shape, dimensions):
    if shape == 'square':
        side = dimensions
        return side * side
    elif shape == 'circle':
        radius = dimensions
        return 3.14159 * radius * radius
    elif shape == 'rectangle':
        length = dimensions[0]
        width = dimensions[1]
        return length * width
    else:
        return None
if __name__ == '__main__':
    shapes_data = {
        'square': 'side',
        'circle': 'radius',
        'rectangle': 'dimensions'
    }
    test_cases = [
        ('square', 5),
        ('circle', 4),
        ('rectangle', (10, 5))
    ]
    for shape, value in test_cases:
        if shape in shapes_data:
            if shape == 'square':
                area = calculate_area(shape, value)
                print(f"Area of {shape} with side {value}: {area}")
            elif shape == 'circle':
                area = calculate_area(shape, value)
                print(f"Area of {shape} with radius {value}: {area}")
            elif shape == 'rectangle':
                area = calculate_area(shape, value)
                print(f"Area of {shape} with dimensions {value}: {area}")
        else:
            print(f"Shape {shape} not supported.")