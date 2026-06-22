def validate_threshold(threshold: int) -> None:
    if not isinstance(threshold, int) or threshold < 0:
        raise ValueError("Threshold must be a non-negative integer.")

def are_lengths_equal_within_threshold(length1: int, length2: int, threshold: int) -> bool:
    validate_threshold(threshold)
    return abs(length1 - length2) <= threshold

if __name__ == '__main__':
    length1 = 400
    length2 = 398
    threshold = 7
    result = are_lengths_equal_within_threshold(length1, length2, threshold)
    print(result)