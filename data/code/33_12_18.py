def calculate_triangle_area(base: float, height: float) -> float:
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return (base * height) / 2

if __name__ == '__main__':
    base_value = 10.0
    height_value = 5.0
    result = calculate_triangle_area(base_value, height_value)
    print(result)