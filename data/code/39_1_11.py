def compute_prism_volume(base_area: float, height: float) -> float:
    if not isinstance(base_area, (int, float)):
        raise TypeError("Base area must be a number")
    if not isinstance(height, (int, float)):
        raise TypeError("Height must be a number")
    if base_area < 0:
        raise ValueError("Base area cannot be negative")
    if height < 0:
        raise ValueError("Height cannot be negative")
    return base_area * height

if __name__ == '__main__':
    hard_coded_base_area = 10.5
    hard_coded_height = 5.0
    volume = compute_prism_volume(hard_coded_base_area, hard_coded_height)
    print(volume)