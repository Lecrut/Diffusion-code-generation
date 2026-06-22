def compute_trapezoid_area(base1, base2, height):
    if not isinstance(base1, (int, float)) or not isinstance(base2, (int, float)) or (not isinstance(height, (int, float))):
        raise TypeError('All inputs must be numeric types.')
    if base1 <= 0 or base2 <= 0 or height <= 0:
        raise ValueError('All inputs must be positive numbers.')
    area = 0.5 * (base1 + base2) * height
    return area
if __name__ == '__main__':
    base1_value = 10.0
    base2_value = 6.0
    height_value = 4.0
    result = compute_trapezoid_area(base1_value, base2_value, height_value)
    print(result)