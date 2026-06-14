def repeating_sequence_generator(sequence, repetitions):
    for _ in range(repetitions):
        yield from sequence
if __name__ == '__main__':
    sample_sequence = [1, 2, 3]
    num_repetitions = 3
    generator = repeating_sequence_generator(sample_sequence, num_repetitions)
    result = list(generator)
    print(result)