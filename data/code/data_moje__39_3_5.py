def calculate_prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    base = 25.5
    height_val = 10.0
    volume = calculate_prism_volume(base, height_val)
    print(volume)