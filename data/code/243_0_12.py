import math

def calculate_circumference(radius: float) -> float:
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return 2 * math.pi * radius

if __name__ == '__main__':
    sample_radius = 5.0
    circumference = calculate_circumference(sample_radius)
    print(f"The circumference of a circle with radius {sample_radius} is {circumference}")