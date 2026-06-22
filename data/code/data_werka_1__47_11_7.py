def calculate_triangle_area(base, height):
    return 0.5 * base * height

if __name__ == '__main__':
    base_length = 18.0
    height_length = 6.0
    triangle_area = calculate_triangle_area(base_length, height_length)
    print(triangle_area)