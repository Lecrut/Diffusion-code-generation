def compute_triangle_area(base, height):
    return 0.5 * base * height

if __name__ == '__main__':
    sample_base = 10
    sample_height = 5
    area = compute_triangle_area(sample_base, sample_height)
    print(area)