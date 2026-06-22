def calculate_parallelogram_areas(base_values, height_values):
    return [b * h for b, h in zip(base_values, height_values)]

if __name__ == '__main__':
    bases = [10, 15, 20, 5]
    heights = [4, 6, 8, 12]
    areas = calculate_parallelogram_areas(bases, heights)
    for i, area in enumerate(areas):
        print(f"Base: {bases[i]}, Height: {heights[i]}, Area: {area}")