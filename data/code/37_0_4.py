PARALLELOGRAM_AREA_MULTIPLIER = 1.0

def calculate_parallelogram_area(base, height):
    return base * height * PARALLELOGRAM_AREA_MULTIPLIER

if __name__ == '__main__':
    sample_base = 7.5
    sample_height = 4.0
    area_result = calculate_parallelogram_area(sample_base, sample_height)
    print(area_result)