def validate_lengths(length1, length2):
    if not (isinstance(length1, (int, float)) and isinstance(length2, (int, float))):
        raise ValueError("Both lengths must be numbers.")
    if length1 <= 0 or length2 <= 0:
        raise ValueError("Both lengths must be positive.")

def calculate_length_ratio(length1, length2):
    validate_lengths(length1, length2)
    minimum = min(length1, length2)
    maximum = max(length1, length2)
    ratio = maximum / minimum
    return ratio

if __name__ == '__main__':
    sample_length1 = 7.0
    sample_length2 = 14.0
    try:
        ratio = calculate_length_ratio(sample_length1, sample_length2)
        print(ratio)
    except ValueError as e:
        print(e)