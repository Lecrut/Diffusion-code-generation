def validate_integers(*values):
    for value in values:
        if not isinstance(value, int):
            raise TypeError(f"Expected integer, got {type(value).__name__}")

def are_lengths_equal_within_threshold(length1: int, length2: int, threshold: int) -> bool:
    validate_integers(length1, length2, threshold)
    return abs(length1 - length2) <= threshold

if __name__ == '__main__':
    try:
        length1 = 400
        length2 = 398
        threshold = 5
        result = are_lengths_equal_within_threshold(length1, length2, threshold)
        print(result)
    except TypeError as e:
        print(e)