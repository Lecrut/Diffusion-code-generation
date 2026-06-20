TRIANGLE_AREA_CONSTANT = 0.5
calculate_area = lambda b, h: TRIANGLE_AREA_CONSTANT * b * h
if __name__ == '__main__':
    base_value = 25
    height_value = 12
    result = calculate_area(base_value, height_value)
    print(result)