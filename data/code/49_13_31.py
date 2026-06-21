def is_within_threshold(length1: int, length2: int, threshold: int) -> bool:
    return abs(length1 - length2) <= threshold

if __name__ == '__main__':
    length1 = 75
    length2 = 80
    threshold = 6
    result = is_within_threshold(length1, length2, threshold)
    print(result)