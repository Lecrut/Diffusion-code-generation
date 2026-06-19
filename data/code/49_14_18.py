def compare_lengths_within_threshold(length_a: int, length_b: int, tolerance: int) -> bool:
    difference = abs(length_a - length_b)
    return difference <= tolerance

if __name__ == '__main__':
    sample_length1 = 250
    sample_length2 = 247
    comparison_threshold = 6
    equality_result = compare_lengths_within_threshold(sample_length1, sample_length2, comparison_threshold)
    print(equality_result)