RECTANGLE_AREA_CONSTANT = 0.5

def calculate_area(base, height):
    return RECTANGLE_AREA_CONSTANT * base * height

if __name__ == '__main__':
    sample_base = 8
    sample_height = 6
    computed_area = calculate_area(sample_base, sample_height)
    print(computed_area)