def validate_length(length):
    if not isinstance(length, (int, float)):
        raise ValueError("Length must be a number")

def compare_lengths(length1, length2):
    validate_length(length1)
    validate_length(length2)
    return max(length1, length2)

if __name__ == '__main__':
    sample_length1 = 35.0
    sample_length2 = 40.5
    try:
        longer_length = compare_lengths(sample_length1, sample_length2)
        print(longer_length)
    except ValueError as e:
        print(e)