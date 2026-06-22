import math

def calculate_circle_area(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radius = 5.0
    area = calculate_circle_area(sample_radius)
    print(area)

    sample_radius_zero = 0
    area_zero = calculate_circle_area(sample_radius_zero)
    print(area_zero)

    try:
        calculate_circle_area(-1)
    except ValueError as e:
        print(str(e))

    try:
        calculate_circle_area("invalid")
    except TypeError as e:
        print(str(e))