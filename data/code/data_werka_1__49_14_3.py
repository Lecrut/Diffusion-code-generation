def are_lengths_equal_within_threshold(length1: int, length2: int, threshold: int) -> bool:
    if not isinstance(length1, int) or not isinstance(length2, int) or not isinstance(threshold, int):
        raise ValueError("All inputs must be integers.")
    return abs(length1 - length2) <= threshold

if __name__ == '__main__':
    try:
        length1 = 200
        length2 = 195
        threshold = 8
        result = are_lengths_equal_within_threshold(length1, length2, threshold)
        print(result)
    except ValueError as e:
        print(e)