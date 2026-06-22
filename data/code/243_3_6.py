import math

def validate_radius(radius):
    if not isinstance(radius, (int, float)) or radius < 0:
        raise ValueError("Radius must be a non-negative number")

def calculate_circumference(radius):
    validate_radius(radius)
    return 2 * math.pi * radius

if __name__ == '__main__':
    sample_radius = 10
    circumference = calculate_circumference(sample_radius)
    print(f"The circumference of a circle with radius {sample_radius} is {circumference:.2f}")