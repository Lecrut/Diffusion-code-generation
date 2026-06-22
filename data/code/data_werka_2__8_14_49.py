import math

def calculate_area(shape, *args):
    if shape == 'rectangle':
        length, width = args
        return length * width
    elif shape == 'circle':
        radius = args[0]
        return math.pi * radius ** 2
    elif shape == 'triangle':
        base, height = args
        return 0.5 * base * height
    else:
        raise ValueError("Unsupported shape")

if __name__ == '__main__':
    rectangle_area = calculate_area('rectangle', 5, 10)
    circle_area = calculate_area('circle', 7)
    triangle_area = calculate_area('triangle', 8, 6)

    print(f"Rectangle area: {rectangle_area}")
    print(f"Circle area: {circle_area}")
    print(f"Triangle area: {triangle_area}")