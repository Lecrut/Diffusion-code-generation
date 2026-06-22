def validate_terms(num_terms):
    if not isinstance(num_terms, int) or num_terms <= 0:
        raise ValueError("Number of terms must be a positive integer")

def generate_doubling_sequence(num_terms):
    validate_terms(num_terms)
    return [2**i for i in range(1, num_terms + 1)]

if __name__ == '__main__':
    sample_value = 5
    result = generate_doubling_sequence(sample_value)
    print(result)