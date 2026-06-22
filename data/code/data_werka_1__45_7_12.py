from math import pi

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return pi * radius ** 2

if __name__ == '__main__':
    sample_radius = 10.0
    area = calculate_circle_area(sample_radius)
    print(area)