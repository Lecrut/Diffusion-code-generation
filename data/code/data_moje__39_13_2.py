def calculate_prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    BASE_AREA = 150.0
    HEIGHT = 20.0
    volume = calculate_prism_volume(BASE_AREA, HEIGHT)
    print(volume)