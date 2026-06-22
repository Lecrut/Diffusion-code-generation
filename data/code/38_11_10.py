import math

PI_OVER_THREE = math.pi / 3.0

def validate_dimensions(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative")
    if not isinstance(radius, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Dimensions must be numeric")

def compute_cone_volume(radius, height):
    validate_dimensions(radius, height)
    base_area = math.pi * (radius ** 2)
    return PI_OVER_THREE * base_area * height

if __name__ == '__main__':
    SAMPLE_RADIUS = 7.5
    SAMPLE_HEIGHT = 15.0
    result = compute_cone_volume(SAMPLE_RADIUS, SAMPLE_HEIGHT)
    print(result)