def first_true(sequence):
    for value in sequence:
        if value:
            yield True

if __name__ == '__main__':
    sample_sequence = [False, False, True, False]
    result = list(first_true(sample_sequence))
    print(result)