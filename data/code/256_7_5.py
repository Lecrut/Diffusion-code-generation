import math
def find_float_range(data):
    if not data:
        return None, None
    min_val = data[0]
    max_val = data[0]
    for x in data:
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x
    return min_val, max_val
if __name__ == '__main__':
    sample_data = [3.1415926535, 1.0, 99.9999999999, -5.5, 0.0, 12345.6789]
    min_r, max_r = find_float_range(sample_data)
    print(f"Minimum value: {min_r}")
    print(f"Maximum value: {max_r}")
    large_sample_data = [1e-308, -1e308, 0.0, math.pi, -math.pi]
    min_l, max_l = find_float_range(large_sample_data)
    print(f"Minimum value (large sample): {min_l}")
    print(f"Maximum value (large sample): {max_l}")