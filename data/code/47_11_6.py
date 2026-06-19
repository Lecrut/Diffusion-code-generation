def calculate_triangle_area(base, height):
    return 0.5 * base * height

if __name__ == '__main__':
    BASE_SAMPLE = 14.0
    HEIGHT_SAMPLE = 6.0
    area = calculate_triangle_area(BASE_SAMPLE, HEIGHT_SAMPLE)
    print(area)