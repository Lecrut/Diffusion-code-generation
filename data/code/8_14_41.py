import math

def validate_shape(shape):
    supported_shapes = ['rectangle', 'circle', 'triangle']
    if shape not in supported_shapes:
        raise ValueError(f"Unsupported shape: {shape}")

def calculate_area(shape, *args):
    validate_shape(shape)
    
    if shape == 'rectangle':
        length, width = args
        return length * width
    elif shape == 'circle':
        radius = args[0]
        return math.pi * radius ** 2
    elif shape == 'triangle':
        base, height = args
        return 0.5 * base * height

if __name__ == '__main__':
    rectangle_area = calculate_area('rectangle', 6, 4)
    circle_area = calculate_area('circle', 8)
    triangle_area = calculate_area('triangle', 10, 2)
    print(f"Rectangle Area: {rectangle_area}")
    print(f"Circle Area: {circle_area}")
    print(f"Triangle Area: {triangle_area}")