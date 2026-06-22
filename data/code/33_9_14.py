import math

def compute_triangle_area(base, height):
    if not isinstance(base, (int, float)) or math.isnan(base) or math.isinf(base):
        raise ValueError("Base must be a valid number")
    if not isinstance(height, (int, float)) or math.isnan(height) or math.isinf(height):
        raise ValueError("Height must be a valid number")
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative")
    return 0.5 * base * height

if __name__ == '__main__':
    base_value = 10
    height_value = 5
    result = compute_triangle_area(base_value, height_value)
    print(result)