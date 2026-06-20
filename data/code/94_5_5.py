def find_first_true(sequence):
    for item in sequence:
        if isinstance(item, bool):
            yield item and True
        else:
            raise ValueError("All items in the sequence must be boolean values")

if __name__ == '__main__':
    seq1 = [False, False, True, False]
    gen1 = find_first_true(seq1)
    try:
        result1 = next(gen1)
        print(f"Sequence: {seq1}, First True found: {result1}")
    except ValueError as e:
        print(e)

    seq2 = [False, False, False]
    gen2 = find_first_true(seq2)
    try:
        result2 = next(gen2)
        print(f"Sequence: {seq2}, First True found: {result2}")
    except ValueError as e:
        print(e)

    seq3 = [True, False, False]
    gen3 = find_first_true(seq3)
    try:
        result3 = next(gen3)
        print(f"Sequence: {seq3}, First True found: {result3}")
    except ValueError as e:
        print(e)