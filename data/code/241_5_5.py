def rectangle_area_generator(dimensions):
    for length, width in dimensions:
        yield length * width
if __name__ == '__main__':
    sample_rectangles = [
        (5, 10),
        (3, 7),
        (12, 4),
        (8, 8)
    ]
    areas = rectangle_area_generator(sample_rectangles)
    for area in areas:
        print(area)