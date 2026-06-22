def generate_sequence(start, length):
    return list(map(lambda x: start + (x * 10), range(length)))

if __name__ == '__main__':
    initial_value = 100
    sequence_length = 15
    result = generate_sequence(initial_value, sequence_length)
    print(result)