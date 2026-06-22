def calculate_parallelogram_areas(bases, heights):
    return [base * height for base, height in zip(bases, heights)]

if __name__ == '__main__':
    bases = [5, 7, 10, 3]
    heights = [4, 6, 8, 2]
    areas = calculate_parallelogram_areas(bases, heights)
    for i, area in enumerate(areas):
        print(f"Parallelogram {i + 1}: base={bases[i]}, height={heights[i]}, area={area}")