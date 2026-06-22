def calculate_prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    base_area = 100
    height = 25
    volume = calculate_prism_volume(base_area, height)
    print(volume)