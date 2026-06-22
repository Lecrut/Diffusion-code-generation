def calculate_triangle_area(base, height):
    return (float(base) * float(height)) / 2.0

if __name__ == '__main__':
    sample_base = 10.0
    sample_height = 5.0
    area = calculate_triangle_area(sample_base, sample_height)
    print(area)