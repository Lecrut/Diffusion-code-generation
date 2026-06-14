def repeat_sequence(sequence, repetition_count):
    return sequence * repetition_count
if __name__ == '__main__':
    sample_sequence = [1, 2]
    repetition = 3
    result = repeat_sequence(sample_sequence, repetition)
    print(result)