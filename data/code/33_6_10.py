def calculate_triangle_area(base: float, height: float) -> float:
    return 0.5 * base * height

if __name__ == '__main__':
    base_value = 10
    height_value = 5
    area = calculate_triangle_area(base_value, height_value)
    print(area)