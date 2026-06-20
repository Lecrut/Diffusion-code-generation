def calculate_scaled_area(base_area: float, scale_factor: float) -> float:
    return base_area * (scale_factor ** 2)

if __name__ == '__main__':
    base = 10.0
    scale = 3.0
    result = calculate_scaled_area(base, scale)
    print(result)