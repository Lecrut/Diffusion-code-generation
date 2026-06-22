import math

def calculate_area(shape, **kwargs):
    if shape == 'circle':
        radius = kwargs.get('radius')
        if radius is None or radius < 0:
            raise ValueError("Radius must be provided and non-negative")
        return math.pi * radius ** 2
    elif shape == 'triangle':
        base = kwargs.get('base')
        height = kwargs.get('height')
        if base is None or height is None or base < 0 or height < 0:
            raise ValueError("Base and height must be provided and non-negative")
        return 0.5 * base * height
    else:
        raise ValueError("Unsupported shape")

if __name__ == '__main__':
    try:
        circle_radius = 3
        circle_area_result = calculate_area('circle', radius=circle_radius)
        print(f"Circle area with radius {circle_radius}: {circle_area_result}")

        triangle_base = 6
        triangle_height = 2
        triangle_area_result = calculate_area('triangle', base=triangle_base, height=triangle_height)
        print(f"Triangle area with base {triangle_base} and height {triangle_height}: {triangle_area_result}")
    except ValueError as e:
        print(e)