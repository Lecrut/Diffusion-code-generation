def generate_growing_sequence(iterations):
    sequence = []
    current_term = 1
    for _ in range(iterations):
        sequence.append(current_term)
        current_term *= 2
    return sequence

if __name__ == '__main__':
    result = generate_growing_sequence(5)
    print(result)