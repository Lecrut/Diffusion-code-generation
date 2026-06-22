def calculate_prism_volume(base_area, height):
    if base_area < 0 or height < 0:
        raise ValueError("Base area and height must be non-negative")
    return base_area * height

if __name__ == '__main__':
    base_area_sample = 25
    height_sample = 10
    volume = calculate_prism_volume(base_area_sample, height_sample)
    print(volume)