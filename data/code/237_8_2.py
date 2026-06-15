def generate_sequence(start_value, growth_factor):
    sequence = []
    current_value = start_value
    for _ in range(10):
        sequence.append(current_value)
        current_value *= growth_factor
    return sequence
if __name__ == '__main__':
    start = 2
    factor = 1.5
    result = generate_sequence(start, factor)
    for term in result:
        print(term)