def compare_lengths_within_threshold(length1: int, length2: int, threshold: int) -> bool:
    if not isinstance(length1, int) or not isinstance(length2, int):
        raise ValueError("Lengths must be integers.")
    if not isinstance(threshold, int) or threshold < 0:
        raise ValueError("Threshold must be a non-negative integer.")
    
    return abs(length1 - length2) <= threshold

if __name__ == '__main__':
    length1 = 400
    length2 = 395
    threshold = 8
    result = compare_lengths_within_threshold(length1, length2, threshold)
    print(result)