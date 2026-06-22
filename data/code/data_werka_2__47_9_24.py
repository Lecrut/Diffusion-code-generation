TRIANGLE_AREA_FORMULA_MULTIPLIER = 0.5

triangle_area = lambda base, height: TRIANGLE_AREA_FORMULA_MULTIPLIER * base * height

if __name__ == '__main__':
    base_value = 15
    height_value = 6
    print(triangle_area(base_value, height_value))