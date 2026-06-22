def compute_triangle_area(base, height):
    return 0.5 * base * height

if __name__ == '__main__':
    base_value = 10
    height_value = 5
    area_result = compute_triangle_area(base_value, height_value)
    print(area_result)
    area_result_2 = compute_triangle_area(7.5, 4)
    print(area_result_2)