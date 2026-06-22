def are_lengths_equal_within_threshold(length1: int, length2: int, threshold: int) -> bool:
    def within_tolerance(a: int, b: int, tol: int) -> bool:
        return abs(a - b) <= tol

    return within_tolerance(length1, length2, threshold)

if __name__ == '__main__':
    sample_values = {
        'length1': 150,
        'length2': 148,
        'threshold': 3
    }
    result = are_lengths_equal_within_threshold(
        sample_values['length1'],
        sample_values['length2'],
        sample_values['threshold']
    )
    print(result)