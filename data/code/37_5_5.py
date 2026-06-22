def calculate_parallelogram_areas(bases, heights):
    return [base * height for base, height in zip(bases, heights)]

if __name__ == '__main__':
    bases = [4, 5, 6]
    heights = [3, 4, 5]
    areas = calculate_parallelogram_areas(bases, heights)
    print(areas)