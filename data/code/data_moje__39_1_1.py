def compute_prism_volume(base_area: float, height: float) -> float:
    return base_area * height

if __name__ == '__main__':
    base_area_value: float = 10.0
    height_value: float = 5.0
    result: float = compute_prism_volume(base_area_value, height_value)
    print(result)