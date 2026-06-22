def calculate_prism_volume(base_area: float, height: float) -> float:
    if base_area < 0 or height < 0:
        raise ValueError("Base area and height must be non-negative.")
    return base_area * height

if __name__ == '__main__':
    base = 25.5
    h = 10.0
    result = calculate_prism_volume(base, h)
    print(result)