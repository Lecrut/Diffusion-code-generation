def calculate_areas(bases, heights):
    return [b * h for b, h in zip(bases, heights)]

if __name__ == '__main__':
    sample_bases = [5, 10, 7, 3]
    sample_heights = [4, 6, 9, 2]
    areas = calculate_areas(sample_bases, sample_heights)
    for i, area in enumerate(areas):
        print(f"Area {i+1}: {area}")