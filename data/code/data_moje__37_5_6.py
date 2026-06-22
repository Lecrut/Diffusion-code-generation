def calculate_parallelogram_areas(base_height_pairs):
    return [base * height for base, height in base_height_pairs]

if __name__ == '__main__':
    pairs = [(5, 10), (7, 8), (12, 5), (3, 15)]
    areas = calculate_parallelogram_areas(pairs)
    for base, height, area in zip(pairs, areas):
        print(f"Base: {base}, Height: {height}, Area: {area}")