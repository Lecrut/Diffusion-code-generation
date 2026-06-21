MAX_THRESHOLD = 10

def are_lengths_equal_within_threshold(length1: int, length2: int, threshold: int) -> bool:
    if threshold > MAX_THRESHOLD:
        raise ValueError(f"Threshold must be less than or equal to {MAX_THRESHOLD}.")
    return abs(length1 - length2) <= threshold

if __name__ == '__main__':
    length1 = 400
    length2 = 398
    threshold = 2
    result = are_lengths_equal_within_threshold(length1, length2, threshold)
    print(result)