BASE_AREA = 10.0
HEIGHT = 5.0

def calculate_prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    volume = calculate_prism_volume(BASE_AREA, HEIGHT)
    print(volume)