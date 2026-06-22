def calculate_triangle_area(base, height):
    return 0.5 * base * height

if __name__ == '__main__':
    base_value = 10.5
    height_value = 8.2
    area = calculate_triangle_area(base_value, height_value)
    print(area)