import math

def compute_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

if __name__ == '__main__':
    try:
        sample_radius = 5
        circle_area = compute_circle_area(sample_radius)
        print(circle_area)
    except ValueError as e:
        print(e)