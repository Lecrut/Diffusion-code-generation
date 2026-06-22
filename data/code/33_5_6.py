HALF = 0.5
_lookup = {}

def triangle_area(base, height):
    key = (base, height)
    if key in _lookup:
        return _lookup[key]
    value = HALF * base * height
    _lookup[key] = value
    return value

if __name__ == '__main__':
    b1 = 12.0
    h1 = 8.0
    a1 = triangle_area(b1, h1)
    print(a1)
    a2 = triangle_area(b1, h1)
    print(a2)
    b2 = 5.5
    h2 = 10.2
    a3 = triangle_area(b2, h2)
    print(a3)