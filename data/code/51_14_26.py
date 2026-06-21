import math
PI = math.pi

def compute_circle_perimeter(radius):
    if radius < 0:
        raise ValueError('Radius cannot be negative')
    return 2 * PI * radius
if __name__ == '__main__':
    sample_radius = 10.0
    perimeter = compute_circle_perimeter(sample_radius)
    print(perimeter)