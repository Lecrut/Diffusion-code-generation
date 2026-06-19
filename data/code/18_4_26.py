def increasing_sequence(sequence):
    previous_value = None
    for value in sequence:
        if previous_value is not None and value > previous_value:
            yield True
        else:
            yield False
        previous_value = value

if __name__ == '__main__':
    sample_sequence = [1, 3, 2, 4, 5]
    result = list(increasing_sequence(sample_sequence))
    print(result)