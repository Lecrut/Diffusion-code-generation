def calculate_prism_volume(base_area: float, height: float) -> float:
    return base_area * height

if __name__ == '__main__':
    base_area_value = 10.5
    height_value = 5.0
    volume_result = calculate_prism_volume(base_area_value, height_value)
    print(volume_result)