def calculate_prism_volume(base_area, height):
    if base_area < 0:
        raise ValueError("Base area must be non-negative.")
    if height < 0:
        raise ValueError("Height must be non-negative.")
    return base_area * height

if __name__ == '__main__':
    base = 10
    h = 5
    volume = calculate_prism_volume(base, h)
    print(volume)