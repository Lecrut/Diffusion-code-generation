def repeating_sequence_generator(sequence, repetitions):
    for _ in range(repetitions):
        for item in sequence:
            yield item
if __name__ == '__main__':
    sample_sequence = [1, 2]
    sample_repetitions = 3
    generator = repeating_sequence_generator(sample_sequence, sample_repetitions)
    result = list(generator)
    print(result)