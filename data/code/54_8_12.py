import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    try:
        sample_radius = 7
        area = calculate_circle_area(sample_radius)
        print(area)
    except ValueError as e:
        print(e)