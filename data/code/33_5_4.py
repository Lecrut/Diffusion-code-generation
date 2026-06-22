CACHE = {}

def compute_triangle_area(base, height):
    key = (base, height)
    if key in CACHE:
        return CACHE[key]
    result = 0.5 * base * height
    CACHE[key] = result
    return result

if __name__ == '__main__':
    b1 = 10.0
    h1 = 5.0
    print(compute_triangle_area(b1, h1))
    b2 = 8.0
    h2 = 3.0
    print(compute_triangle_area(b2, h2))
    print(compute_triangle_area(b1, h1))