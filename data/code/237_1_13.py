def arithmetic_progression(start, difference, terms):
    if not all(isinstance(i, (int, float)) and i >= 0 for i in [start, difference, terms]):
        raise ValueError("All input values must be non-negative numbers.")
    
    return [start + i * difference for i in range(terms)]

if __name__ == '__main__':
    sample_start = 3
    sample_difference = 4
    sample_terms = 15
    
    sequence = arithmetic_progression(sample_start, sample_difference, sample_terms)
    print(sequence)