def calculate_triangle_area(base, height):
    if base <= 0:
        raise ValueError("Base must be positive")
    if height <= 0:
        raise ValueError("Height must be positive")
    return 0.5 * base * height

if __name__ == '__main__':
    try:
        base = 10
        height = 5
        area = calculate_triangle_area(base, height)
        print(area)
    except ValueError as e:
        print(e)