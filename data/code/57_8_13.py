def generate_fibonacci_sequence(limit_index):
    if limit_index < 0:
        raise ValueError('Index must be a non-negative integer.')
    if limit_index == 0:
        return [0]
    if limit_index == 1:
        return [0, 1]
    sequence = [0, 1]
    for i in range(2, limit_index + 1):
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence
if __name__ == '__main__':
    print(generate_fibonacci_sequence(10))
    print(generate_fibonacci_sequence(0))
    print(generate_fibonacci_sequence(1))