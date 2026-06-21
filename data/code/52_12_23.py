import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    area = math.pi * (radius ** 2)
    return area

if __name__ == '__main__':
    sample_radius = 7.5
    circle_area = calculate_circle_area(sample_radius)
    print(circle_area)