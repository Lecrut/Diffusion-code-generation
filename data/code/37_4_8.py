UNIT_MULTIPLIERS = {'m': 1.0, 'cm': 0.0001, 'mm': 0.000001}

def get_parallelogram_area(base, height):
    return base * height

if __name__ == '__main__':
    base_val = 8.0
    height_val = 4.5
    computed_area = get_parallelogram_area(base_val, height_val)
    print(computed_area)