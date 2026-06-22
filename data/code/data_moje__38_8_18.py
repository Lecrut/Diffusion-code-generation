import math

def _validate_dimensions(radius, height):
    if not isinstance(radius, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Dimensions must be numbers")
    if radius <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive")

def cone_volume(radius, height):
    _validate_dimensions(radius, height)
    base_area = math.pi * (radius ** 2)
    return (base_area * height) / 3.0

if __name__ == '__main__':
    result = cone_volume(8, 11)
    print(f"{result:.2f}")