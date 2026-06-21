import math

def compute_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    area = math.pi * (radius ** 2)
    return area

if __name__ == '__main__':
    try:
        sample_radius = 5
        result_area = compute_circle_area(sample_radius)
        print(f"The area of the circle with radius {sample_radius} is: {result_area}")
    except ValueError as e:
        print(e)