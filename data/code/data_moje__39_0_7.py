def calculate_prism_volume(base_area, height):
    if base_area <= 0:
        raise ValueError("Base area must be positive")
    if height <= 0:
        raise ValueError("Height must be positive")
    return base_area * height

if __name__ == '__main__':
    base_area = 25.0
    height = 10.0
    result = calculate_prism_volume(base_area, height)
    print(result)