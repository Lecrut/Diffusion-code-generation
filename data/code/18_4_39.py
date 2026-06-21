def increasing_sequence(sequence):
    previous = None
    for value in sequence:
        if previous is not None and value > previous:
            yield True
        else:
            yield False
        previous = value

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 2, 4, 5, 3]
    for result in increasing_sequence(sample_sequence):
        print(result)