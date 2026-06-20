def first_true(sequence):
    for value in sequence:
        if value:
            yield True
            break

if __name__ == '__main__':
    sample_sequence = [False, False, True, False]
    result = next(first_true(sample_sequence))
    print(result)