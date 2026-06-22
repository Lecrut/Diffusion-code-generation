import math

_area_cache = {}

def compute_triangle_area(base, height):
    if base < 0 or height < 0:
        return 0.0
    
    key = (base, height)
    if key in _area_cache:
        return _area_cache[key]
    
    area = 0.5 * base * height
    _area_cache[key] = area
    return area

if __name__ == '__main__':
    base_value = 10
    height_value = 5
    result = compute_triangle_area(base_value, height_value)
    print(result)
    
    repeated_base = 10
    repeated_height = 5
    repeated_result = compute_triangle_area(repeated_base, repeated_height)
    print(repeated_result)