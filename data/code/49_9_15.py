def validate_length(length):
    if not isinstance(length, (int, float)):
        raise ValueError("Length must be an integer or float.")
    if length < 0:
        raise ValueError("Length must be non-negative.")

def compare_lengths(length1, length2):
    validate_length(length1)
    validate_length(length2)
    return (min(length1, length2), max(length1, length2))

if __name__ == '__main__':
    sample_length1 = 45
    sample_length2 = 30
    result = compare_lengths(sample_length1, sample_length2)
    print(result)