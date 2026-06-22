def increasing_sequence_generator(sequence):
    previous_value = None
    for current_value in sequence:
        if previous_value is not None and current_value > previous_value:
            yield True
        else:
            yield False
        previous_value = current_value

if __name__ == '__main__':
    sample_sequence = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]
    for result in increasing_sequence_generator(sample_sequence):
        print(result)