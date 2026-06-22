import math

def calculate_area(shape, **kwargs):
    def square(side):
        return side * side

    def circle(radius):
        return math.pi * radius * radius

    area_functions = {
        'square': square,
        'circle': circle,
    }

    if shape not in area_functions:
        raise ValueError(f"Unsupported shape: {shape}")

    return area_functions[shape](**kwargs)

if __name__ == '__main__':
    try:
        side_length = 8
        square_area = calculate_area('square', side=side_length)
        radius_length = 5
        circle_area = calculate_area('circle', radius=radius_length)
        print(f"Area of square with side {side_length}: {square_area}")
        print(f"Area of circle with radius {radius_length}: {circle_area}")
    except ValueError as e:
        print(e)