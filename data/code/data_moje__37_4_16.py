def get_parallelogram_area(base, height):
    return base * height

if __name__ == '__main__':
    base_value = 12.0
    height_value = 6.5
    computed_area = get_parallelogram_area(base_value, height_value)
    print(computed_area)