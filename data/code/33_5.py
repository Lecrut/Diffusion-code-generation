import math

_cache = {}

def compute_triangle_area(base, height):
    if (base, height) in _cache:
        return _cache[(base, height)]
    result = 0.5 * base * height
    _cache[(base, height)] = result
    return result

if __name__ == '__main__':
    base_val = 10.0
    height_val = 5.0
    area = compute_triangle_area(base_val, height_val)
    print(area)
    repeated_area = compute_triangle_area(base_val, height_val)
    print(repeated_area)