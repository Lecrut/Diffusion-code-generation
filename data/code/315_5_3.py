def generate_repeating_sequence(N, start, step):
    sequence = []
    for i in range(N):
        term = start + (i % step)
        sequence.append(term)
    return sequence
if __name__ == '__main__':
    N = 20
    start_value = 1
    step_value = 3
    result = generate_repeating_sequence(N, start_value, step_value)
    print(result)