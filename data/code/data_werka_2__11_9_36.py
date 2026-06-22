def calculate_ratios(length_pairs):
    ratios = []
    for length1, length2 in length_pairs:
        if length2 == 0:
            continue
        ratio = length1 / length2
        ratios.append(ratio)
    return ratios

if __name__ == '__main__':
    sample_values = [(10, 2), (5, 0), (8, 4), (0, 3)]
    result = calculate_ratios(sample_values)
    print(result)