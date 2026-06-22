def generate_arithmetic_progression(start=5, difference=3, terms=15):
    sequence = []
    for i in range(terms):
        term = start + i * difference
        sequence.append(term)
    return sequence

if __name__ == '__main__':
    first_term = 7
    common_difference = 4
    num_terms = 20
    progression = generate_arithmetic_progression(first_term, common_difference, num_terms)
    print(progression)