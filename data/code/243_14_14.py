import math

def calculate_circle_perimeter(radius):
    if not isinstance(radius, (int, float)) or radius < 0:
        raise ValueError("Radius must be a non-negative number.")
    return 2 * math.pi * radius

if __name__ == '__main__':
    sample_radius = 5.0
    perimeter = calculate_circle_perimeter(sample_radius)
    print(f"Perimeter of the circle with radius {sample_radius} is {perimeter:.2f}")