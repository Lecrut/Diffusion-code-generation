def calculate_pairwise_average(pairs):
    return [(pair1 + pair2) / 2.0 for pair1, pair2 in pairs]

if __name__ == '__main__':
    sample_pairs = [(1, 2), (3, 4), (5, 6)]
    average_result = calculate_pairwise_average(sample_pairs)
    print(average_result)