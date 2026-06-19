MAX_THRESHOLD = 10

def compare_lengths_within_threshold(length1: int, length2: int, threshold: int) -> bool:
    if threshold > MAX_THRESHOLD:
        raise ValueError("Threshold exceeds maximum allowed value.")
    return abs(length1 - length2) <= threshold

if __name__ == '__main__':
    length1 = 400
    length2 = 398
    threshold = 5
    result = compare_lengths_within_threshold(length1, length2, threshold)
    print(result)