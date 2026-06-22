def calculate_prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    base = 15.0
    height = 10.0
    volume = calculate_prism_volume(base, height)
    print(volume)