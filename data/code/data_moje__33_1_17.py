TRIANGLE_AREA_FACTOR = 0.5

def get_triangle_area(base, height):
    return base * height * TRIANGLE_AREA_FACTOR

if __name__ == '__main__':
    TEST_BASE = 12
    TEST_HEIGHT = 8
    computed_area = get_triangle_area(TEST_BASE, TEST_HEIGHT)
    print(computed_area)