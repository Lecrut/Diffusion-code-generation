def increasing_sequence(seq):
    prev = None
    for value in seq:
        if prev is not None and value > prev:
            yield True
        else:
            yield False
        prev = value

if __name__ == '__main__':
    sample_values = [1, 3, 2, 4, 5]
    result = list(increasing_sequence(sample_values))
    print(result)