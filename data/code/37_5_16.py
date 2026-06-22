def calculate_parallelogram_areas(bases_heights):
    return [base * height for base, height in bases_heights]

if __name__ == '__main__':
    bases_heights = [(4, 5), (6, 3), (10, 2)]
    areas = calculate_parallelogram_areas(bases_heights)
    for area in areas:
        print(area)