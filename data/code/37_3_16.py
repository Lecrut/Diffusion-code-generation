AREA_MULTIPLIER = 1.0

def calculate_parallelogram_area(base, height):
    return float(base * height * AREA_MULTIPLIER)

if __name__ == '__main__':
    base_val = 12.5
    height_val = 8.0
    computed_area = calculate_parallelogram_area(base_val, height_val)
    print(computed_area)