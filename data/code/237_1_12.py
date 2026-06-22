def generate_arithmetic_sequence(start, difference, terms):
    return [start + i * difference for i in range(terms)]

if __name__ == '__main__':
    first_term = 3
    common_difference = 4
    num_terms = 15
    sequence = generate_arithmetic_sequence(first_term, common_difference, num_terms)
    print(sequence)