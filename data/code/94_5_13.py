def first_true(sequence):
    for value in sequence:
        if value:
            yield True

if __name__ == '__main__':
    seq1 = [False, False, True, False]
    gen1 = first_true(seq1)
    result1 = next(gen1, False)
    print(f"Sequence: {seq1}, First True found: {result1}")

    seq2 = [False, False, False]
    gen2 = first_true(seq2)
    result2 = next(gen2, False)
    print(f"Sequence: {seq2}, First True found: {result2}")

    seq3 = [True, False, True]
    gen3 = first_true(seq3)
    result3 = next(gen3, False)
    print(f"Sequence: {seq3}, First True found: {result3}")