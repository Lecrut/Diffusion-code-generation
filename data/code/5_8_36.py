def validate_lengths(length1, length2):
    if not isinstance(length1, (float, int)) or not isinstance(length2, (float, int)):
        raise ValueError("Both inputs must be numbers.")

def compare_lengths(length1, length2):
    validate_lengths(length1, length2)
    difference = abs(length1 - length2)
    
    if length1 > length2:
        result = "First length is greater"
    elif length2 > length1:
        result = "Second length is greater"
    else:
        result = "Both lengths are equal"
    
    return (difference, result)

if __name__ == '__main__':
    sample_length1 = 7.5
    sample_length2 = 2.3
    print(compare_lengths(sample_length1, sample_length2))