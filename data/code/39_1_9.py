def compute_prism_volume(base_area, height):
    if not isinstance(base_area, (int, float)):
        raise TypeError("base_area must be a number")
    if not isinstance(height, (int, float)):
        raise TypeError("height must be a number")
    if base_area <= 0:
        raise ValueError("base_area must be positive")
    if height <= 0:
        raise ValueError("height must be positive")
    return base_area * height

if __name__ == '__main__':
    base_area = 10
    height = 5
    volume = compute_prism_volume(base_area, height)
    print(volume)