import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radii = [5, 0, 3.14]
    for r in sample_radii:
        area = calculate_circle_area(r)
        print(area)

    try:
        calculate_circle_area(-1)
    except ValueError as e:
        print(e)