def repeat_sequence(sequence, repetitions):
    return '\n'.join([sequence for _ in range(repetitions)])

if __name__ == '__main__':
    sample_sequence = 'Hello World'
    sample_repetitions = 100
    result = repeat_sequence(sample_sequence, sample_repetitions)
    print(result)