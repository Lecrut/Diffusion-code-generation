SAMPLE_BASE = 7
SAMPLE_HEIGHT = 4

def calculate_parallelogram_area(base, height):
    return base * height

if __name__ == '__main__':
    area = calculate_parallelogram_area(SAMPLE_BASE, SAMPLE_HEIGHT)
    print(area)