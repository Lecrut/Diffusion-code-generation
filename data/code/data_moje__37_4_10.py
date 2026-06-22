def get_parallelogram_area(base, height):
    if base <= 0:
        return 0.0
    if height <= 0:
        return 0.0
    return base * height

if __name__ == '__main__':
    SAMPLE_BASE = 12.5
    SAMPLE_HEIGHT = 8.0
    print(get_parallelogram_area(SAMPLE_BASE, SAMPLE_HEIGHT))