def generate_sequence(start, length):
    return list(map(lambda x: start + 10 * x, range(length)))

if __name__ == '__main__':
    initial_value = 100
    sequence_length = 15
    generated_sequence = generate_sequence(initial_value, sequence_length)
    print(generated_sequence)