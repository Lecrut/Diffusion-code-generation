SEQUENCE_START = 1
SEQUENCE_MULTIPLIER = 2

def generate_doubling_sequence(num_terms):
    return [SEQUENCE_START * (SEQUENCE_MULTIPLIER ** i) for i in range(num_terms)]

if __name__ == '__main__':
    sample_value = 5
    result = generate_doubling_sequence(sample_value)
    print(result)