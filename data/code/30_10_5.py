import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radius = 5.0
    area = calculate_circle_area(sample_radius)
    print(area)

    sample_radius_2 = 10.0
    area_2 = calculate_circle_area(sample_radius_2)
    print(area_2)

    sample_radius_3 = 1.0
    area_3 = calculate_circle_area(sample_radius_3)
    print(area_3)

    try:
        calculate_circle_area(-1.0)
    except ValueError as e:
        print(str(e))