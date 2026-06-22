def increasing_sequence(sequence):
    previous = None
    for current in sequence:
        if previous is not None and current <= previous:
            yield False
        else:
            yield True
        previous = current

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 5, 3, 6]
    result = list(increasing_sequence(sample_sequence))
    print(result)