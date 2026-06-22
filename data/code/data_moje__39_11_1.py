def calculate_prism_volume(base_area, height):
    if base_area <= 0 or height <= 0:
        raise ValueError("Base area and height must be positive numbers.")
    return base_area * height

if __name__ == '__main__':
    print(calculate_prism_volume(10, 5))
    print(calculate_prism_volume(25.5, 4))
    print(calculate_prism_volume(100, 2.5))