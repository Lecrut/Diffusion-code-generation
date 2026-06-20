def are_lengths_equal_within_threshold(length1: int, length2: int, threshold: int = 0) -> bool:
    return abs(length1 - length2) <= threshold

if __name__ == '__main__':
    print(are_lengths_equal_within_threshold(10, 12, 2))
    print(are_lengths_equal_within_threshold(10, 15, 2))
    print(are_lengths_equal_within_threshold(100, 100, 5))