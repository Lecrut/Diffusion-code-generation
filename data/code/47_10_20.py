TRIANGLE_AREA_FACTOR = 0.5

triangle_area = lambda base, height: TRIANGLE_AREA_FACTOR * base * height

if __name__ == '__main__':
    sample_base = 14
    sample_height = 6
    print(triangle_area(sample_base, sample_height))