import math

def compute_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    test_radius = 10
    try:
        area_result = compute_circle_area(test_radius)
        print(area_result)
    except ValueError as e:
        print(e)