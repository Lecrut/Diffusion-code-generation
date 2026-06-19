def calculate_area_of_triangle(base, height):
    return 0.5 * base * height

if __name__ == '__main__':
    sample_base = 8.5
    sample_height = 3.2
    triangle_area = calculate_area_of_triangle(sample_base, sample_height)
    print(triangle_area)