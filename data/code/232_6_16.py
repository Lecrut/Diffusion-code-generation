if __name__ == '__main__':
    initial_value = 100
    sequence_length = 15

    growing_sequence = list(map(lambda x: initial_value + x, range(sequence_length)))

    for term in growing_sequence:
        print(term)