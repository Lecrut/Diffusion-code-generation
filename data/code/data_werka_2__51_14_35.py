import math

def compute_circle_perimeter(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return 2 * math.pi * radius

if __name__ == '__main__':
    sample_radius = 4.5
    perimeter = compute_circle_perimeter(sample_radius)
    print(perimeter)