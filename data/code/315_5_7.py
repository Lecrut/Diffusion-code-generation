def generate_repeating_sequence(n, start, diff):
    sequence = []
    for i in range(n):
        index = i % 3
        term = start + index * diff
        sequence.append(term)
    return sequence
if __name__ == '__main__':
    N = 10
    START_TERM = 1
    DIFFERENCE = 1
    result = generate_repeating_sequence(N, START_TERM, DIFFERENCE)
    print(result)