def calculate_parallelogram_area(base, height):
    product = base * height
    return product

if __name__ == '__main__':
    sample_base = 4.0
    sample_height = 2.5
    computed_area = calculate_parallelogram_area(sample_base, sample_height)
    print(computed_area)