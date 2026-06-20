def find_first_true(sequence):
    for item in sequence:
        if item:
            yield True
            return

if __name__ == '__main__':
    seq1 = [False, False, True, False]
    gen1 = find_first_true(seq1)
    result1 = next(gen1, False)
    print(f"Sequence: {seq1}, First True found: {result1}")

    seq2 = [False, False, False]
    gen2 = find_first_true(seq2)
    result2 = next(gen2, False)
    print(f"Sequence: {seq2}, First True found: {result2}")

    seq3 = [True, False, False]
    gen3 = find_first_true(seq3)
    result3 = next(gen3, False)
    print(f"Sequence: {seq3}, First True found: {result3}")