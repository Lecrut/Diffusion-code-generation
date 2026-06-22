def calculate_triangle_area(base: float, height: float) -> float:
    if base < 0 or height < 0:
        raise ValueError("Base and height must be non-negative")
    return 0.5 * base * height

if __name__ == '__main__':
    area = calculate_triangle_area(10.0, 5.0)
    print(area)
    area2 = calculate_triangle_area(7.5, 4.2)
    print(area2)
    area3 = calculate_triangle_area(0.0, 100.0)
    print(area3)