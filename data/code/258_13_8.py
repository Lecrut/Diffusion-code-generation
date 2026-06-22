def compute_averages(pair1, pair2):
    return tuple((x + y) / 2 for x, y in zip(pair1, pair2))

if __name__ == '__main__':
    sample_pair1 = (8, 16, 24)
    sample_pair2 = (32, 40, 48)
    result = compute_averages(sample_pair1, sample_pair2)
    print(result)