def compare_lengths(length1, length2, epsilon=1e-09):
    if not (isinstance(length1, float) and isinstance(length2, float)):
        raise ValueError('Both lengths must be floating-point numbers.')
    
    difference = abs(length1 - length2)
    is_within_tolerance = difference < epsilon
    
    if is_within_tolerance:
        return None
    elif length1 > length2:
        return length1
    else:
        return length2

if __name__ == '__main__':
    sample_length_a = 2.718281828459045
    sample_length_b = 2.718281828459046
    result = compare_lengths(sample_length_a, sample_length_b)
    print(result)