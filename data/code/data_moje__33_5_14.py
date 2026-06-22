import math

_cache = {}

def triangle_area(base, height):
    key = (base, height)
    if key in _cache:
        return _cache[key]
    result = 0.5 * base * height
    _cache[key] = result
    return result

if __name__ == '__main__':
    base = 10
    height = 5
    area = triangle_area(base, height)
    print(area)