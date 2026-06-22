def calculate_prism_volume(base_area: float, height: float) -> float:
    return base_area * height

if __name__ == '__main__':
    sample_base_area = 10.0
    sample_height = 5.0
    volume = calculate_prism_volume(sample_base_area, sample_height)
    print(volume)