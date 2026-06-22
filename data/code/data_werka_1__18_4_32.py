def increasing_sequence_generator(sequence):
    previous_value = None
    for value in sequence:
        if previous_value is not None and value > previous_value:
            yield True
        else:
            yield False
        previous_value = value

if __name__ == '__main__':
    sample_sequence = [1, 3, 2, 4, 5, 6, 7, 8, 6]
    generator = increasing_sequence_generator(sample_sequence)
    results = list(generator)
    print(results)