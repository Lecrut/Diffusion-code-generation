def validate_lengths(length1: int, length2: int, threshold: int):
    if not all(isinstance(x, int) and x >= 0 for x in (length1, length2, threshold)):
        raise ValueError("All inputs must be non-negative integers.")

def are_lengths_equal_within_threshold(length1: int, length2: int, threshold: int) -> bool:
    validate_lengths(length1, length2, threshold)
    return abs(length1 - length2) <= threshold

if __name__ == '__main__':
    try:
        length1 = 400
        length2 = 398
        threshold = 7
        result = are_lengths_equal_within_threshold(length1, length2, threshold)
        print(result)
    except ValueError as e:
        print(e)