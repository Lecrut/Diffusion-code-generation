def generate_arithmetic_progression(start, difference, terms):
    current_term = start
    for _ in range(terms):
        yield current_term
        current_term += difference

if __name__ == '__main__':
    first_term = 3
    common_difference = 4
    num_terms = 15
    sequence_generator = generate_arithmetic_progression(first_term, common_difference, num_terms)
    result_list = list(sequence_generator)
    print(result_list)