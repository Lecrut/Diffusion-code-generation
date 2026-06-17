def generate_repeating_sequence(N, start, step):
    sequence = []
    cycle_length = 0
    current_value = start
    if step == 0:
        return [start] * N
    while len(sequence) < N:
        if cycle_length == 0:
            sequence.append(current_value)
            cycle_length += 1
            current_value += step
        else:
            index = (len(sequence) - 1) % cycle_length
            sequence.append(sequence[index])
    return sequence
if __name__ == '__main__':
    N = 20
    start = 1
    step = 1
    result = generate_repeating_sequence(N, start, step)
    print(result)