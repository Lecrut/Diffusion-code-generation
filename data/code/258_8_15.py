def compute_averages(pair_generator):
    return tuple((a + b) / 2 for a, b in pair_generator)

if __name__ == '__main__':
    sample_data = [
        (1, 2),
        (3, 4),
        (5, 6)
    ]
    print(compute_averages(sample_data))