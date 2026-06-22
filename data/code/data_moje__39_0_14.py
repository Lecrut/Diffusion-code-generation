def calculate_prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    base_area = 10.5
    height = 4.2
    volume = calculate_prism_volume(base_area, height)
    print(volume)