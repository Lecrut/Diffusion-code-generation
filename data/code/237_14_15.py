def generate_doubling_sequence(num_terms):
    if num_terms < 1:
        raise ValueError("Number of terms must be at least 1")
    
    sequence = [2**i for i in range(1, num_terms + 1)]
    return sequence

if __name__ == '__main__':
    sample_value = 5
    try:
        result = generate_doubling_sequence(sample_value)
        print(result)
    except ValueError as e:
        print(e)