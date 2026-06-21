def validate_lengths(length1, length2):
    if length1 <= 0 or length2 <= 0:
        raise ValueError("Both lengths must be positive")

def calculate_ratio(length1, length2):
    validate_lengths(length1, length2)
    return length1 / length2

if __name__ == '__main__':
    try:
        sample_length1 = 15
        sample_length2 = 3
        ratio_result = calculate_ratio(sample_length1, sample_length2)
        print(ratio_result)
    except ValueError as e:
        print(e)