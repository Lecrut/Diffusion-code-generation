def calculate_ratios(length_pairs):
    def compute_ratio(pair):
        length1, length2 = pair
        if length2 == 0:
            return None
        return length1 / length2

    ratios = [compute_ratio(pair) for pair in length_pairs if compute_ratio(pair) is not None]
    return ratios

if __name__ == '__main__':
    sample_length_pairs = [(10, 2), (5, 0), (8, 4), (3, 3)]
    result = calculate_ratios(sample_length_pairs)
    print(result)