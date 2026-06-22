def compute_square_areas(side_lengths):
    return [side ** 2 for side in side_lengths]

if __name__ == '__main__':
    sample_lengths = [2, 4, 5, 8, 10]
    results = compute_square_areas(sample_lengths)
    print(results)