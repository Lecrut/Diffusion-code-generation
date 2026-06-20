def has_first_true(sequence):
    return any(sequence)

if __name__ == '__main__':
    seq1 = [False, False, True, False]
    result1 = has_first_true(seq1)
    print(f"Sequence: {seq1}, First True found: {result1}")
    
    seq2 = [False, False, False]
    result2 = has_first_true(seq2)
    print(f"Sequence: {seq2}, First True found: {result2}")
    
    seq3 = [True, False, False]
    result3 = has_first_true(seq3)
    print(f"Sequence: {seq3}, First True found: {result3}")