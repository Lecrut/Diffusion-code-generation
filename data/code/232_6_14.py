def generate_sequence(initial_value, length):
    return list(map(lambda x: initial_value + (x * 10), range(length)))

if __name__ == '__main__':
    initial_value = 100
    length = 15
    sequence = generate_sequence(initial_value, length)
    print(sequence)