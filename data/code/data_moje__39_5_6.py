def calculate_prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    base = 50
    height_val = 12
    volume = calculate_prism_volume(base, height_val)
    print(volume)