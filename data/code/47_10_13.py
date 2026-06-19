TRIANGLE_HALF = 0.5

triangle_area = lambda base, height: TRIANGLE_HALF * base * height

if __name__ == '__main__':
    BASE_VALUE = 20
    HEIGHT_VALUE = 6
    print(triangle_area(BASE_VALUE, HEIGHT_VALUE))