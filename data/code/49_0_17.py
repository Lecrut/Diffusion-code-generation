def validate_length(length):
    if not isinstance(length, (int, float)):
        raise ValueError("Length must be an integer or float")

def compare_lengths(length1, length2):
    validate_length(length1)
    validate_length(length2)
    
    result = {
        'length1': length1,
        'length2': length2,
        'is_length1_greater': length1 > length2
    }
    return result

if __name__ == '__main__':
    sample_length1 = 25.0
    sample_length2 = 30
    result = compare_lengths(sample_length1, sample_length2)
    print(result)