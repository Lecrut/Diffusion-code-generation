BASE = 7
HEIGHT = 4
AREA_MULTIPLIER = 1

def calculate_parallelogram_area(b, h):
    return b * h * AREA_MULTIPLIER

if __name__ == '__main__':
    area = calculate_parallelogram_area(BASE, HEIGHT)
    print(area)