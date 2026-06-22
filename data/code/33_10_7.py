def calculate_triangle_area(base: float, height: float) -> float:
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative numbers.")
    return (base * height) / 2

if __name__ == '__main__':
    base = 10
    height = 5
    area = calculate_triangle_area(base, height)
    print(area)