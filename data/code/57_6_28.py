import math

def calculate_area(shape, dimensions):
    if shape == 'rectangle':
        length, width = dimensions
        return length * width
    elif shape == 'circle':
        radius = dimensions[0]
        return math.pi * radius ** 2
    elif shape == 'triangle':
        base, height = dimensions
        return 0.5 * base * height
    else:
        raise ValueError(f"Unsupported shape: {shape}")

if __name__ == '__main__':
    sample_shapes = [
        ('rectangle', (4, 5)),
        ('circle', (3,)),
        ('triangle', (6, 4))
    ]

    for shape, dimensions in sample_shapes:
        area = calculate_area(shape, dimensions)
        print(f"The area of a {shape} with dimensions {dimensions} is {area}")