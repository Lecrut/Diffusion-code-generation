def rectangle_area_generator(dimensions):
    for length, width in dimensions:
        yield length * width
if __name__ == '__main__':
    sample_dimensions = [
        (5, 10),
        (3, 7),
        (12, 2),
        (8, 5)
    ]
    area_generator = rectangle_area_generator(sample_dimensions)
    results = list(area_generator)
    print(results)