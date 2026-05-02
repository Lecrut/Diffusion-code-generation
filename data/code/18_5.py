def greater_than_previous(sequence):
    if not sequence:
        return
    previous = sequence[0]
    for current in sequence[1:]:
        if current > previous:
            yield True
        previous = current
if __name__ == '__main__':
    sample_sequence = [1, 3, 2, 5, 5, 4]
    generator = greater_than_previous(sample_sequence)
    results = list(generator)
    print(results)