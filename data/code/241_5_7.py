def rectangle_area_generator(dimensions):
    for length, width in dimensions:
        yield length * width
if __name__ == '__main__':
    sample_dimensions = [
        (2, 3),
        (5, 10),
        (1, 1),
        (7, 4)
    ]
    area_generator = rectangle_area_generator(sample_dimensions)
    areas = list(area_generator)
    print(areas)