def _compute_area(base, height):
    return 0.5 * base * height

_cache = {}

def get_triangle_area(base, height):
    key = (base, height)
    if key in _cache:
        return _cache[key]
    area = _compute_area(base, height)
    _cache[key] = area
    return area

if __name__ == '__main__':
    base_val = 10
    height_val = 5
    result = get_triangle_area(base_val, height_val)
    print(result)