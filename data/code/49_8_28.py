def compare_lengths(length1, length2):
    if not isinstance(length1, (int, float)) or not isinstance(length2, (int, float)):
        raise ValueError("Both lengths must be numbers")
    
    min_length = length1 if length1 < length2 else length2
    max_length = length1 if length1 > length2 else length2
    
    return (min_length, max_length)

if __name__ == '__main__':
    sample_length1 = 35
    sample_length2 = 40
    result = compare_lengths(sample_length1, sample_length2)
    print(result)