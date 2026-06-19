def validate_integers(*args):
    for arg in args:
        if not isinstance(arg, int):
            raise ValueError("All inputs must be integers.")

def are_lengths_equal_within_threshold(length1: int, length2: int, threshold: int) -> bool:
    validate_integers(length1, length2, threshold)
    return abs(length1 - length2) <= threshold

if __name__ == '__main__':
    try:
        length1 = 400
        length2 = 398
        threshold = 10
        result = are_lengths_equal_within_threshold(length1, length2, threshold)
        print(result)
    except ValueError as e:
        print(e)