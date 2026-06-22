def generate_sequence(limit):
    sequence = [1, 2]
    while len(sequence) < limit:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence[:limit]

if __name__ == '__main__':
    sample_limit = 15
    result = generate_sequence(sample_limit)
    print(*result)