def calculate_triangle_area(base: float, height: float) -> float:
    return 0.5 * base * height

if __name__ == '__main__':
    sample_base: float = 10.0
    sample_height: float = 5.0
    area: float = calculate_triangle_area(sample_base, sample_height)
    print(area)