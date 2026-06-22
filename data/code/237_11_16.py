def generate_arithmetic_progression(start=5, difference=3, terms=15):
    sequence = []
    current_term = start
    for _ in range(terms):
        sequence.append(current_term)
        current_term += difference
    return sequence

if __name__ == '__main__':
    initial_value = 3
    step_size = 4
    number_of_elements = 20
    progression = generate_arithmetic_progression(initial_value, step_size, number_of_elements)
    print(progression)