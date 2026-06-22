def generate_doubling_sequence(num_terms):
    if num_terms <= 0:
        raise ValueError("Number of terms must be greater than zero")
    return [2**i for i in range(1, num_terms + 1)]

if __name__ == '__main__':
    sample_value = 5
    result = generate_doubling_sequence(sample_value)
    print(result)