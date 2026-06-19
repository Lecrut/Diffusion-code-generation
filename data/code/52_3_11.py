import math

SHAPE_AREAS = {
    'rectangle': lambda length, width: length * width,
    'circle': lambda radius: math.pi * (radius ** 2),
    'triangle': lambda base, height: 0.5 * base * height
}

def calculate_area(shape, *args):
    if shape in SHAPE_AREAS:
        return SHAPE_AREAS[shape](*args)
    else:
        raise ValueError("Unsupported shape")

if __name__ == '__main__':
    rectangle_area = calculate_area('rectangle', 6, 4)
    circle_area = calculate_area('circle', 5)
    triangle_area = calculate_area('triangle', 7, 3)
    print(f"Rectangle area: {rectangle_area}")
    print(f"Circle area: {circle_area}")
    print(f"Triangle area: {triangle_area}")