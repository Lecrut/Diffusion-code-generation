def compare_lengths_within_threshold(length1: int, length2: int, threshold: int) -> bool:
    difference = abs(length1 - length2)
    return difference <= threshold

if __name__ == '__main__':
    first_length = 400
    second_length = 398
    tolerance = 6
    equality_result = compare_lengths_within_threshold(first_length, second_length, tolerance)
    print(equality_result)