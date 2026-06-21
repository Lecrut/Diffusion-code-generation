def compute_square_areas(sides):
    return [side * side for side in sides]

if __name__ == '__main__':
    sample_lengths = [2, 4, 5, 8]
    results = compute_square_areas(sample_lengths)
    print(results)