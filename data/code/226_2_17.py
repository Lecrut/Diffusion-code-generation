def repeat_sequence(sequence, repetitions):
    if not isinstance(sequence, str) or not sequence:
        raise ValueError("Sequence must be a non-empty string")
    if not isinstance(repetitions, int) or repetitions < 0:
        raise ValueError("Repetitions must be a non-negative integer")

    result = [sequence] * repetitions
    return '\n'.join(result)

if __name__ == '__main__':
    sample_sequence = 'Hello World'
    sample_repetitions = 100
    repeated_string = repeat_sequence(sample_sequence, sample_repetitions)
    print(repeated_string)