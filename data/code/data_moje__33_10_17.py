def calculate_triangle_area(base, height):
    return float(base * height / 2)

if __name__ == '__main__':
    base_value = 10
    height_value = 5
    area = calculate_triangle_area(base_value, height_value)
    print(area)