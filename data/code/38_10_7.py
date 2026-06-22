import math

def _validate_dimensions(radius, height):
    if not isinstance(radius, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Dimensions must be numeric")
    if radius <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive")

def compute_cone_volume(radius, height):
    _validate_dimensions(radius, height)
    return (1.0 / 3.0) * math.pi * (radius ** 2) * height

if __name__ == '__main__':
    result = compute_cone_volume(5, 10)
    print(result)