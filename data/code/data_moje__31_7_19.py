def compute_square_areas(side_lengths):
    return [side * side for side in side_lengths]

if __name__ == '__main__':
    sample_side_lengths = [3, 5, 7, 10]
    results = compute_square_areas(sample_side_lengths)
    print(results)