def compute_triangle_area(base, height):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")
    if not isinstance(height, (int, float)):
        raise TypeError("Height must be a number")
    if base < 0:
        raise ValueError("Base must be non-negative")
    if height < 0:
        raise ValueError("Height must be non-negative")
    return 0.5 * base * height

if __name__ == '__main__':
    result = compute_triangle_area(10, 5)
    print(result)
    result2 = compute_triangle_area(7.5, 4.2)
    print(result2)
    try:
        compute_triangle_area("invalid", 5)
    except TypeError as e:
        print(e)
    try:
        compute_triangle_area(-3, 5)
    except ValueError as e:
        print(e)