def calculate_ratios(length_pairs):
    ratios = []
    for length1, length2 in length_pairs:
        if length2 != 0:
            ratio = length1 / length2
            ratios.append(ratio)
    return ratios

if __name__ == '__main__':
    sample_length_pairs = [(10, 5), (20, 0), (30, 15), (40, 2)]
    result = calculate_ratios(sample_length_pairs)
    print(result)