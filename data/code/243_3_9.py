import math

def calculate_circumference(radius):
    if radius <= 0:
        raise ValueError("Radius must be a positive number")
    return 2 * math.pi * radius

if __name__ == '__main__':
    sample_radius = 10
    try:
        circumference = calculate_circumference(sample_radius)
        print(f"The circumference of a circle with radius {sample_radius} is {circumference:.2f}")
    except ValueError as e:
        print(e)