def compare_lengths_within_threshold(length1: int, length2: int, threshold: int) -> bool:
    difference = abs(length1 - length2)
    return difference <= threshold

if __name__ == '__main__':
    sample_length1 = 400
    sample_length2 = 398
    sample_threshold = 10
    is_within_threshold = compare_lengths_within_threshold(sample_length1, sample_length2, sample_threshold)
    print(is_within_threshold)