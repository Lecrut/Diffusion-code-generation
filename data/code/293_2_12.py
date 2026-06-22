import math

def calculate_area(shape_type, *params):
    if shape_type == 'circle':
        radius = params[0]
        return math.pi * radius ** 2
    elif shape_type == 'square':
        side_length = params[0]
        return side_length ** 2
    elif shape_type == 'rectangle':
        length, width = params
        return length * width
    else:
        raise ValueError("Unsupported shape type")

if __name__ == '__main__':
    circle_area = calculate_area('circle', 5)
    square_area = calculate_area('square', 4)
    rectangle_area = calculate_area('rectangle', 3, 2)
    
    print(f"Circle area: {circle_area}")
    print(f"Square area: {square_area}")
    print(f"Rectangle area: {rectangle_area}")