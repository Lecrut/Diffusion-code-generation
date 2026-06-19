import math

def compute_circle_perimeter(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    
    diameter = 2 * radius
    perimeter = math.pi * diameter
    return perimeter

if __name__ == '__main__':
    sample_radius = 10.0
    try:
        circle_perimeter = compute_circle_perimeter(sample_radius)
        print(circle_perimeter)
    except ValueError as e:
        print(e)