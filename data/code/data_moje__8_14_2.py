def calculate_scaled_area(base_area: float, scale_factor: float) -> float:
    return base_area * (scale_factor ** 2)

if __name__ == '__main__':
    result = calculate_scaled_area(10.0, 2.0)
    print(result)