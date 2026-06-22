def calculate_triangle_area(base, height):
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative")
    return 0.5 * base * height

if __name__ == '__main__':
    print(calculate_triangle_area(5, 10))
    print(calculate_triangle_area(7, 3))
    try:
        calculate_triangle_area(-2, 5)
    except ValueError as e:
        print(e)