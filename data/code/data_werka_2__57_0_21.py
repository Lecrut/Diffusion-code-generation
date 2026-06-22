import math

def calculate_area_circle(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    sample_radius = 10.0
    area = calculate_area_circle(sample_radius)
    print(f"The area of the circle with radius {sample_radius} is {area}")