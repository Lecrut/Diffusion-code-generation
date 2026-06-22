def calculate_areas(base_values, height_values):
    return [b * h for b, h in zip(base_values, height_values)]

if __name__ == '__main__':
    bases = [5, 10, 15]
    heights = [3, 7, 2]
    areas = calculate_areas(bases, heights)
    for area in areas:
        print(area)