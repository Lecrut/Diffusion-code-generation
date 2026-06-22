import math
import numbers

def calculate_triangle_area(base, height):
    if not isinstance(base, numbers.Number) or not isinstance(height, numbers.Number):
        raise TypeError("Base and height must be numeric types.")
    if math.isnan(base) or math.isnan(height):
        raise ValueError("Base and height cannot be NaN.")
    if math.isinf(base) or math.isinf(height):
        raise ValueError("Base and height cannot be infinite.")
    if base < 0:
        raise ValueError("Base cannot be negative.")
    if height < 0:
        raise ValueError("Height cannot be negative.")
    return 0.5 * base * height

if __name__ == '__main__':
    base_value = 10.0
    height_value = 5.0
    area = calculate_triangle_area(base_value, height_value)
    print(area)