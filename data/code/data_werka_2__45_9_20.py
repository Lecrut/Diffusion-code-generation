import math

PI = math.pi

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return PI * radius ** 2

if __name__ == '__main__':
    try:
        sample_radius = 10.5
        area = calculate_circle_area(sample_radius)
        print(f"The area of a circle with radius {sample_radius} is {area}")
    except ValueError as e:
        print(e)