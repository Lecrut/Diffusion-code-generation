def repeat_sequence(sequence, count):
    result = []
    for _ in range(count):
        result.extend(sequence)
    return result
if __name__ == '__main__':
    sample_sequence = [1, 2]
    repetition_count = 3
    repeated_list = repeat_sequence(sample_sequence, repetition_count)
    print(repeated_list)