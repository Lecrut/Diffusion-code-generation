def compute_triangle_area(base, height):
    try:
        base = float(base)
        height = float(height)
    except (TypeError, ValueError):
        return 0.0
    if base <= 0 or height <= 0:
        return 0.0
    return 0.5 * base * height

if __name__ == '__main__':
    result = compute_triangle_area(10, 5)
    print(result)