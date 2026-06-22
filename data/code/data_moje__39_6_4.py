def compute_prism_volume(base_area, height):
    if base_area < 0 or height < 0:
        raise ValueError("Base area and height must be non-negative.")
    return base_area * height

if __name__ == '__main__':
    base_area = 50.0
    height = 12.5
    volume = compute_prism_volume(base_area, height)
    print(volume)