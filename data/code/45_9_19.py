import math

PI = 3.141592653589793

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return PI * radius ** 2

if __name__ == '__main__':
    sample_radius = 10.0
    try:
        area = calculate_circle_area(sample_radius)
        print(area)
    except ValueError as e:
        print(e)