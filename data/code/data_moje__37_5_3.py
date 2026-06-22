def calculate_parallelogram_areas(bases, heights):
    return [base * height for base, height in zip(bases, heights)]

if __name__ == '__main__':
    bases = [5, 10, 7.5]
    heights = [4, 8, 3.2]
    areas = calculate_parallelogram_areas(bases, heights)
    print(areas)