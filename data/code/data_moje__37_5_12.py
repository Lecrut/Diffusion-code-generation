def calculate_parallelogram_areas(bases, heights):
    return [b * h for b, h in zip(bases, heights)]

if __name__ == '__main__':
    bases = [5, 10, 3.5, 8]
    heights = [4, 6, 2.5, 12]
    areas = calculate_parallelogram_areas(bases, heights)
    for b, h, area in zip(bases, heights, areas):
        print(f"Base: {b}, Height: {h}, Area: {area}")