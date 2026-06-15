def repeat_sequence(sequence, repetition_count):
    result = []
    for _ in range(repetition_count):
        result.extend(sequence)
    return result
if __name__ == '__main__':
    sample_sequence = [1, 2]
    sample_repetition = 3
    repeated_list = repeat_sequence(sample_sequence, sample_repetition)
    print(repeated_list)