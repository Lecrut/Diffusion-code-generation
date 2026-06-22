def triangle_area(base, height):
    try:
        b = float(base)
        h = float(height)
    except (TypeError, ValueError):
        return 0.0
    if b < 0 or h < 0:
        return 0.0
    return 0.5 * b * h

if __name__ == '__main__':
    print(triangle_area(10, 5))
    print(triangle_area(7, 3))
    print(triangle_area('abc', 5))
    print(triangle_area(10, None))
    print(triangle_area(-5, 10))
    print(triangle_area(0, 5))
    print(triangle_area(3.5, 4.2))