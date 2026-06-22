def calculate_triangle_area(base: float, height: float) -> float:
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative")
    return 0.5 * base * height

if __name__ == '__main__':
    base = 10.0
    height = 5.0
    area = calculate_triangle_area(base, height)
    print(area)