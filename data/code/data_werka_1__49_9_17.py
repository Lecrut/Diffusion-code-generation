def compare_lengths(length1, length2):
    if not isinstance(length1, (int, float)) or not isinstance(length2, (int, float)):
        raise ValueError("Both arguments must be numbers.")
    if length1 < 0 or length2 < 0:
        raise ValueError("Lengths must be non-negative.")
    return (min(length1, length2), max(length1, length2))

if __name__ == '__main__':
    try:
        sample_length1 = 30
        sample_length2 = 45
        result = compare_lengths(sample_length1, sample_length2)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")