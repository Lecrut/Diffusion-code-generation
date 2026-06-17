def generate_repeating_sequence(n, start, diff):
    sequence = []
    for i in range(n):
        index = i % 3
        term = start + index * diff
        sequence.append(term)
    return sequence
if __name__ == '__main__':
    N = 10
    start_value = 1
    difference = 1
    result = generate_repeating_sequence(N, start_value, difference)
    print(result)