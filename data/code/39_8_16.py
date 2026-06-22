def calculate_prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    base = 25.0
    h = 10.0
    volume = calculate_prism_volume(base, h)
    print(volume)