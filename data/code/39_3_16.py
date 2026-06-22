def calculate_prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    base_area = 50.0
    height = 12.5
    volume = calculate_prism_volume(base_area, height)
    print(volume)