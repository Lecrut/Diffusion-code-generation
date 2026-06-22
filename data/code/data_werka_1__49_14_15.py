def compare_lengths_within_threshold(length1: int, length2: int, threshold: int) -> bool:
    diff = abs(length1 - length2)
    return diff <= threshold

if __name__ == '__main__':
    length_a = 400
    length_b = 403
    tolerance = 4
    print(compare_lengths_within_threshold(length_a, length_b, tolerance))