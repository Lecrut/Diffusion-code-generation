def increasing_sequence(sequence):
    previous = None
    for value in sequence:
        if previous is not None and value > previous:
            yield True
        else:
            yield False
        previous = value

if __name__ == '__main__':
    sample_values = [1, 3, 2, 4, 5]
    result = list(increasing_sequence(sample_values))
    print(result)