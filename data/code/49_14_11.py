def compare_lengths_within_threshold(length1: int, length2: int, threshold: int) -> bool:
    difference = abs(length1 - length2)
    return difference <= threshold

if __name__ == '__main__':
    length1 = 400
    length2 = 398
    threshold = 6
    result = compare_lengths_within_threshold(length1, length2, threshold)
    print(result)