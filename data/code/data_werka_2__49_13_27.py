def are_lengths_equal_within_threshold(length1: int, length2: int, threshold: int) -> bool:
    if threshold < 0:
        raise ValueError("Threshold must be a non-negative integer.")
    return abs(length1 - length2) <= threshold

if __name__ == '__main__':
    length1 = 400
    length2 = 407
    threshold = 8
    result = are_lengths_equal_within_threshold(length1, length2, threshold)
    print(result)