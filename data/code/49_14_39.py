def compare_lengths(length1, length2):
    if not isinstance(length1, (int, float)) or not isinstance(length2, (int, float)):
        raise ValueError("Both lengths must be numbers")
    return max(length1, length2)

if __name__ == '__main__':
    sample_length1 = 45.6
    sample_length2 = 38.9
    try:
        longer_length = compare_lengths(sample_length1, sample_length2)
        print(longer_length)
    except ValueError as e:
        print(e)