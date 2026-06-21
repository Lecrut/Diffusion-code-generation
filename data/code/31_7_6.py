def compute_square_areas(sides):
    return [side ** 2 for side in sides]

if __name__ == '__main__':
    sample_lengths = [1, 2, 3, 4, 5]
    results = compute_square_areas(sample_lengths)
    print(results)