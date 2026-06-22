import math

def calculate_area(shape, **kwargs):
    if shape == 'rectangle':
        return kwargs['length'] * kwargs['width']
    elif shape == 'circle':
        return math.pi * (kwargs['radius'] ** 2)
    elif shape == 'triangle':
        return 0.5 * kwargs['base'] * kwargs['height']
    else:
        raise ValueError("Unsupported shape")

if __name__ == '__main__':
    rectangle_area = calculate_area('rectangle', length=5, width=3)
    circle_area = calculate_area('circle', radius=4)
    triangle_area = calculate_area('triangle', base=6, height=2)

    print(f"Rectangle area: {rectangle_area}")
    print(f"Circle area: {circle_area}")
    print(f"Triangle area: {triangle_area}")