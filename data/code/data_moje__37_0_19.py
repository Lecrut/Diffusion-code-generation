def calculate_parallelogram_area(base, height):
    return base * height

def get_sample_base():
    return 8.5

def get_sample_height():
    return 4.0

if __name__ == '__main__':
    base_val = get_sample_base()
    height_val = get_sample_height()
    area = calculate_parallelogram_area(base_val, height_val)
    print(area)