def is_strictly_increasing(sequence):
    previous_value = None
    for current_value in sequence:
        if previous_value is not None and current_value <= previous_value:
            yield False
        else:
            yield True
        previous_value = current_value

if __name__ == '__main__':
    sample_sequence = [1, 3, 2, 4, 5]
    result = list(is_strictly_increasing(sample_sequence))
    print(result)