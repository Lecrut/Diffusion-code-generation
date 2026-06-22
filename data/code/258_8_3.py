def compute_average_pairs(pair_generator):
    return tuple((a + b) / 2 for a, b in pair_generator)

if __name__ == '__main__':
    sample_data = [
        (7, 8),
        (9, 10),
        (11, 12)
    ]
    result = compute_average_pairs(sample_data)
    print(result)