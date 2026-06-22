def triangle_area(base, height):
    COEFFICIENT = 1 / 2
    return base * height * COEFFICIENT

if __name__ == '__main__':
    BASE_VALUE = 8
    HEIGHT_VALUE = 4
    computed_value = triangle_area(BASE_VALUE, HEIGHT_VALUE)
    print(computed_value)