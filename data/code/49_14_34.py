def compare_lengths(length1, length2):
    if not isinstance(length1, (int, float)) or not isinstance(length2, (int, float)):
        raise ValueError("Both lengths must be numbers")
    
    return max(length1, length2)

if __name__ == '__main__':
    SAMPLE_LENGTH_1 = 18.4
    SAMPLE_LENGTH_2 = 25.6
    try:
        longer_length = compare_lengths(SAMPLE_LENGTH_1, SAMPLE_LENGTH_2)
        print(longer_length)
    except ValueError as e:
        print(e)