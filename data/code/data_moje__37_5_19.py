def calculate_parallelogram_areas(base_height_pairs):
    return [b * h for b, h in base_height_pairs]

if __name__ == '__main__':
    bases_and_heights = [(5, 10), (7, 3), (12, 4)]
    areas = calculate_parallelogram_areas(bases_and_heights)
    for area in areas:
        print(area)