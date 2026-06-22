def calculate_prism_volume(base_area: float, height: float) -> float:
    return base_area * height

if __name__ == '__main__':
    hard_coded_base_area = 10.5
    hard_coded_height = 5.2
    volume = calculate_prism_volume(hard_coded_base_area, hard_coded_height)
    print(volume)