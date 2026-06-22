def generate_doubling_sequence(num_terms):
    if not isinstance(num_terms, int) or num_terms <= 0:
        raise ValueError("num_terms must be a positive integer")
    
    sequence = [1]
    for _ in range(1, num_terms):
        sequence.append(sequence[-1] * 2)
    
    return sequence

if __name__ == '__main__':
    sample_value = 5
    result = generate_doubling_sequence(sample_value)
    print(result)