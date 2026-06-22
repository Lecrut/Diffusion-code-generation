def compare_lengths(length1, length2):
    try:
        if not (isinstance(length1, (int, float)) and isinstance(length2, (int, float))):
            raise ValueError("Both lengths must be numbers.")
        if length1 < 0 or length2 < 0:
            raise ValueError("Lengths must be non-negative.")
        return (min(length1, length2), max(length1, length2))
    except ValueError as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    sample_length1 = 15
    sample_length2 = 20
    result = compare_lengths(sample_length1, sample_length2)
    if result:
        print(result)