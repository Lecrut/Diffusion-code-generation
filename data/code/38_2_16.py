import math

def compute_cone_volume(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Radius and height must be non-negative")
    if not isinstance(radius, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Radius and height must be numbers")
    base_area = math.pi * (radius ** 2)
    return base_area * height / 3.0

if __name__ == '__main__':
    sample_radius = 3
    sample_height = 7
    result = compute_cone_volume(sample_radius, sample_height)
    print(result)