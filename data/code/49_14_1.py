def are_lengths_equal_within_threshold(length1: int, length2: int, threshold: int) -> bool:
    return abs(length1 - length2) <= threshold

if __name__ == '__main__':
    length1 = 100
    length2 = 105
    threshold = 5
    result = are_lengths_equal_within_threshold(length1, length2, threshold)
    print(result)