def compare_lengths(length1, length2, epsilon=1e-09):
    if not (isinstance(length1, float) and isinstance(length2, float)):
        raise ValueError('Both lengths must be floating-point numbers.')
    
    def is_within_tolerance(a, b, tol):
        return abs(a - b) < tol
    
    if is_within_tolerance(length1, length2, epsilon):
        return None
    elif length1 > length2:
        return length1
    else:
        return length2

if __name__ == '__main__':
    sample_lengths = {
        'length_a': 3.141592653589793,
        'length_b': 3.141592653589794,
        'length_c': 3.141592653589795
    }
    
    result_ab = compare_lengths(sample_lengths['length_a'], sample_lengths['length_b'])
    result_ac = compare_lengths(sample_lengths['length_a'], sample_lengths['length_c'])
    
    print("Result between length_a and length_b:", result_ab)
    print("Result between length_a and length_c:", result_ac)