def calculate_parallelogram_areas(base_height_pairs):
    return [base * height for base, height in base_height_pairs]

if __name__ == '__main__':
    samples = [(10, 5), (8, 4), (12, 7)]
    areas = calculate_parallelogram_areas(samples)
    for pair, area in zip(samples, areas):
        print(f"Base: {pair[0]}, Height: {pair[1]}, Area: {area}")