def increasing_sequence(sequence):
    previous_value = None
    for current_value in sequence:
        if previous_value is not None and current_value > previous_value:
            yield True
        else:
            yield False
        previous_value = current_value

if __name__ == '__main__':
    sample_sequence = [10, 20, 30, 25, 40, 50, 45]
    result_list = list(increasing_sequence(sample_sequence))
    print(result_list)