BASE_MULTIPLIER = 1.0

def calculate_parallelogram_area(base, height):
    return base * height * BASE_MULTIPLIER

if __name__ == '__main__':
    SAMPLE_BASE = 12.5
    SAMPLE_HEIGHT = 4.0
    area = calculate_parallelogram_area(SAMPLE_BASE, SAMPLE_HEIGHT)
    print(area)