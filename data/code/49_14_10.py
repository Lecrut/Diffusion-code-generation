def compare_lengths_within_threshold(length1: int, length2: int, threshold: int) -> bool:
    return abs(length1 - length2) <= threshold

if __name__ == '__main__':
    sample_values = {
        'length1': 400,
        'length2': 398,
        'threshold': 7
    }
    result = compare_lengths_within_threshold(**sample_values)
    print(result)