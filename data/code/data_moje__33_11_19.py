def get_triangle_area(base_length, height_length):
    half = 0.5
    product = base_length * height_length
    return product * half

if __name__ == '__main__':
    sample_base = 12
    sample_height = 8
    calculated_area = get_triangle_area(sample_base, sample_height)
    print(calculated_area)