import math

def compute_circle_perimeter(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return 2 * math.pi * radius

if __name__ == '__main__':
    hard_coded_radius = 10.0
    try:
        circle_perimeter = compute_circle_perimeter(hard_coded_radius)
        print(circle_perimeter)
    except ValueError as e:
        print(e)