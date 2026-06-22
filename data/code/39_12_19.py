PRISM_BASE_AREA = 128.5
PRISM_HEIGHT = 15.75
SCALE_FACTOR = 1.0

def calculate_prism_volume(base_area, height):
    return base_area * height * SCALE_FACTOR

if __name__ == '__main__':
    volume = calculate_prism_volume(PRISM_BASE_AREA, PRISM_HEIGHT)
    print(volume)