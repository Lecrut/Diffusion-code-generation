import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    sample_radius_1 = 5
    sample_radius_2 = -3
    print(calculate_circle_area(sample_radius_1))
    try:
        print(calculate_circle_area(sample_radius_2))
    except ValueError as e:
        print(e)