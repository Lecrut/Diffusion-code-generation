import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    sample_radius = 10
    print(calculate_circle_area(sample_radius))