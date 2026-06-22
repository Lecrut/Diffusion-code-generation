import math

def compute_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius * radius

if __name__ == '__main__':
    positive_radius = 7
    zero_radius = 0
    negative_radius = -5

    area_positive = compute_circle_area(positive_radius)
    print(area_positive)

    area_zero = compute_circle_area(zero_radius)
    print(area_zero)

    try:
        compute_circle_area(negative_radius)
    except ValueError as error:
        print(str(error))