def calculate_triangle_area(base, height):
    return (lambda b, h: 0.5 * b * h)(base, height)

if __name__ == '__main__':
    sample_base = 10
    sample_height = 5
    area = calculate_triangle_area(sample_base, sample_height)
    print(area)