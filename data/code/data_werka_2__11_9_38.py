def calculate_ratios(length_pairs):
    ratios = []
    for length1, length2 in length_pairs:
        try:
            if length2 == 0:
                raise ValueError("Denominator cannot be zero.")
            ratio = length1 / length2
            ratios.append(ratio)
        except ValueError as e:
            print(f"Error: {e}")
    return ratios

if __name__ == '__main__':
    sample_length_pairs = [(10, 2), (5, 0), (8, 4), (3, 3)]
    result = calculate_ratios(sample_length_pairs)
    print(result)