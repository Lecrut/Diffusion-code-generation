def compute_prism_volume(base_area: float, height: float) -> float:
    if base_area < 0 or height < 0:
        raise ValueError("Base area and height must be non-negative.")
    return base_area * height

if __name__ == '__main__':
    base_area = 10.0
    height = 5.0
    result = compute_prism_volume(base_area, height)
    print(result)