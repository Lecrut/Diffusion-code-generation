MAX_TERMS = 10

def generate_doubling_sequence(num_terms):
    if num_terms > MAX_TERMS:
        raise ValueError("Number of terms exceeds maximum allowed.")
    return [2**i for i in range(num_terms)]

if __name__ == '__main__':
    sample_value = 5
    result = generate_doubling_sequence(sample_value)
    print(result)