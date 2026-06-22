def generate_arithmetic_progression(start=5, difference=3, terms=15):
    sequence = []
    current_term = start
    for _ in range(terms):
        sequence.append(current_term)
        current_term += difference
    return sequence

if __name__ == '__main__':
    first_value = 7
    step_size = 4
    term_count = 20
    progression = generate_arithmetic_progression(first_value, step_size, term_count)
    print(progression)