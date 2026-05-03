def calculate_ratios(length_pairs):
    ratios = []
    for length1, length2 in length_pairs:
        if length2 != 0:
            ratios.append(length1 / length2)
    return ratios
if __name__ == '__main__':
    sample_data = [(10, 2), (5, 0), (20, 4), (3, 0), (15, 3)]
    result = calculate_ratios(sample_data)
    print(result)